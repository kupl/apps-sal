class Solution:

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        if not K or K == 1:
            return sum(A)
        if not A:
            return 0
        dp = [0] * len(A)
        for (index, num) in enumerate(A):
            possible = []
            for group in range(K):
                if index - group >= 0:
                    if index - group - 1 >= 0:
                        previous = dp[index - group - 1]
                    else:
                        previous = 0
                    possible.append(previous + max(A[index - group:index + 1]) * (group + 1))
            dp[index] = max(possible)
        return dp[-1]
