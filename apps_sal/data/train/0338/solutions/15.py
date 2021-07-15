# 1397. Find All Good Strings
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        e_len = len(evil)
        par = [0] * e_len
        
        for i in range(1, e_len):
            j = par[i-1]
            while j and evil[i] != evil[j]:
                j = par[j-1]
            j += int(evil[i] == evil[j])
            par[i] = j
            
        mod = (10 ** 9) + 7
        @lru_cache(None)
        def rec(cur, ei, sm, bg):
            if ei == e_len:
                return 0
            if cur == n:
                return 1
            
            ans = 0
            st = ord('a') if bg else ord(s1[cur])
            ed = ord('z') if sm else ord(s2[cur])
                
            for i in range(st, ed + 1):
                if i == ord(evil[ei]):
                    new_ei = ei + 1
                else:
                    new_ei = ei
                    while new_ei and evil[new_ei] != chr(i):
                        new_ei = par[new_ei - 1]
                    if evil[new_ei] == chr(i):
                        new_ei += 1
                ans += rec(cur+1, new_ei, sm | (i < ord(s2[cur])), bg | (i > ord(s1[cur])))
                if ans >= mod:
                    ans -= mod
            return ans
        
        return rec(0, 0, False, False)%mod
