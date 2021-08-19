class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        dp = {}

        def f(i, k):
            if (i, k) not in dp:
                if k == 1:
                    dp[i, k] = sum(A[i:]) / (n - i)
                else:
                    dp[i, k] = max([sum(A[i:j]) / (j - i) + f(j, k - 1) for j in range(i + 1, n - k + 2)])
            return dp[i, k]
        return f(0, K)
