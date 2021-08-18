class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        indexes = {A[0]: 0}
        n = len(A)

        dp = [[2 for i in range(n)] for j in range(n)]

        max_len = 2

        for i in range(1, n - 1):
            indexes[A[i]] = i
            for j in range(i + 1, n):
                diff = A[j] - A[i]
                if diff in indexes:
                    dp[i][j] = 1 + dp[indexes[diff]][i]
                    max_len = max(max_len, dp[i][j])

        if max_len > 2:
            return max_len
        return 0
