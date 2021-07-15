class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s) 
        def dp(i, cur):
            nonlocal ans            
            if len(cur) + n-i < ans: return
            if i >= n: ans = max(ans, len(cur))                
            l = n-i
            for k in range(1, l+1):
                cand = s[i:i+k]
                if cand not in cur: 
                    cur.append(cand)
                    dp(i+k, cur)
                    cur.pop()            
        ans, cur = 0, []
        dp(0, cur)
        return ans
