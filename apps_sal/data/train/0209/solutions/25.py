class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        if (n - 1) % (K - 1):
            return -1
        
        s = [0]
        for num in stones:
            s.append(s[-1] + num)
        
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = float('inf')
                for m in range(i, j, K - 1):
                    dp[i][j] = min(dp[i][j], dp[i][m] + dp[m + 1][j] + (0 if (j - i) % (K - 1) else s[j + 1] - s[i]))
        
        return -1 if dp[0][-1] == float('inf') else dp[0][-1]
        
        
        @functools.lru_cache(None)
        def f(i, j):
            if i == j:
                return 0
            ans = float('inf')
            m = i
            while m < j:
                ans = min(ans, f(i, m) + f(m + 1, j) + (0 if (j - i) % (K - 1) else s[j + 1] - s[i]))
                m += K - 1
                
            return ans
        
        ans = f(0, n - 1)
        return -1 if ans == float('inf') else ans
