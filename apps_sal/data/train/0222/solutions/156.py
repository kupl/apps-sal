import bisect


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        dp = [0] * n
        for i in range(0, n):
            dp[i] = [0] * n

        record = {elem: idx for idx, elem in enumerate(A)}

        for i in range(0, n - 1):
            for j in range(i + 1, n):
                target = A[j] - A[i]
                if target in record and record[target] < i:
                    k = record[target]
                    dp[i][j] = max(dp[i][j], dp[k][i] + 1)
        ans = 0
        for i in range(0, n):
            for j in range(0, n):
                ans = max(ans, dp[i][j])

        if ans > 0:
            return ans + 2
        return 0
