class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def count_changes(_s):            
            m = len(_s) // 2
            return sum([int(c1 != c2) for c1, c2 in zip(_s[:m], _s[::-1][:m])])
            
        n = len(s)
        if n == k:
            return 0
        
        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
        for i in range(1, n + 1):
            dp[1][i] = count_changes(s[:i])
        
        for _k in range(2, k + 1):
            for i in range(_k, n + 1):
                for j in range(_k - 1, i):
                    dp[_k][i] = min(dp[_k][i], dp[_k - 1][j] + count_changes(s[j:i]))
        
        return dp[k][n]

