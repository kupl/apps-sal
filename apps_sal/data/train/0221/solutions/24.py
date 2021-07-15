class Solution:
    def longestDupSubstring(self, S: str) -> str:
        
        def check(s, L):
            n = len(s)
            BASE = 26
            MOD = 1 << 61 - 1
            P = pow(26, L, MOD)
            cur = 0
            seen = defaultdict(list)
            
            for i in range(len(s)):
                cur = (cur*BASE + ord(s[i]) - ord('a')) % MOD
                if i >= L:
                    cur = (cur - (ord(s[i-L]) - ord('a')) * P) % MOD
                
                if i >= L - 1:
                    if cur in seen:
                        cur_str = s[i-L+1:i+1]
                        for j in seen[cur]:
                            pre_str = s[j-L+1:j+1]
                            if cur_str == pre_str:
                                return cur_str
                    seen[cur].append(i)       
            return ''
            
            
        lo, hi = 1, len(S)
        ans = ''
        while lo < hi:
            mid = (lo + hi) // 2
            temp = check(S, mid)
            if temp:
                ans = temp
                lo = mid + 1
            else:
                hi = mid

        return ans

