class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        dp = [[2] * len(A) for _ in range(len(A))]
        d = {}
        for (i, num) in enumerate(A):
            d[num] = i
        res = 2
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                if diff in d and d[diff] < i:
                    dp[i][j] = dp[d[diff]][i] + 1
                    res = max(res, dp[i][j])
        return res if res >= 3 else 0
