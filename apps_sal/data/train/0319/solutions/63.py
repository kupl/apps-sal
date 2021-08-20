class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [float('-inf')] * n

        def dfs(i):
            if i >= n:
                return 0
            if dp[i] != float('-inf'):
                return dp[i]
            ssum = 0
            for j in range(3):
                if i + j < n:
                    ssum += stoneValue[i + j]
                    dp[i] = max(dp[i], ssum - dfs(i + j + 1))
            return dp[i]
        score = dfs(0)
        if score > 0:
            return 'Alice'
        elif score < 0:
            return 'Bob'
        return 'Tie'
