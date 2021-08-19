class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        dp = [[2] * n for _ in range(n)]

        idxs = {num: i for i, num in enumerate(A)}

        result = 0
        for j in range(2, n):
            for i in range(1, j):
                target = A[j] - A[i]
                if target in idxs and target < A[i]:
                    # A[j] - A[i] 在 A 中且 在 A[i] 的左方
                    dp[i][j] = dp[idxs[target]][i] + 1
                    result = max(result, dp[i][j])

        return result
