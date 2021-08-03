class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:

        A.sort()

        dp = [1 for _ in range(len(A))]

        for i in range(len(A)):

            for j in range(i):

                time, remain = divmod(A[i], A[j])

                if remain == 0 and time in A:

                    dp[i] += (dp[j] * dp[A.index(time)])

        return sum(dp) % (10**9 + 7)
