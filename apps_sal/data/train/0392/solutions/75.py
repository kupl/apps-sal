class Solution:
    def numWays(self, s: str) -> int:
        cnt = s.count('1')
        if cnt % 3 != 0:
            return 0
        if cnt == 0:
            ans = 0
            for i in range(1, len(s) - 1):
                ans += i
            return ans % (10**9 + 7)
        
        l = r = 1
        c = 0
        
        for i, n in enumerate(s):
            c += 1 if n == '1' else 0
            
            if  c == cnt / 3 and n == '0':
                l += 1
            elif c == (cnt / 3) * 2 and n == '0':
                r += 1
        
        print((l, r))
        return l * r % (10**9 + 7)

