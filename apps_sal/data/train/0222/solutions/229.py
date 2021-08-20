class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        N = len(A)
        dp = [[2] * N for _ in range(N)]
        a = {val: i for (i, val) in enumerate(A)}
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                if diff in a and a[diff] < j:
                    dp[i][j] = max(dp[i][j], dp[j][a[diff]] + 1)
        res = max([max(i) for i in dp])
        return res if res > 2 else 0
