class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        
        
        
        n = len(s)
        def dp(cur, ss):
            # print(ss)
            if cur == n-1:
                return len(set(ss.split()))
            cur += 1
            return max(dp(cur, ss + s[cur]), dp(cur, ss + ' ' + s[cur]))
        return dp(0, s[0])
