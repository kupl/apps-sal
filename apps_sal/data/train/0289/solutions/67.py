class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        dp = [[-1, -1] for i in range(len(A))]
        # print(dp)

        l = L - 1
        dp[l][0] = sum(A[0:L])
        l += 1
        while l < len(A):
            dp[l][0] = dp[l - 1][0] - A[l - L] + A[l]
            l += 1

        m = M - 1
        dp[m][1] = sum(A[0:M])
        m += 1
        while m < len(A):
            dp[m][1] = dp[m - 1][1] - A[m - M] + A[m]
            m += 1

        # dp.sort(reverse=True, key=lambda x: x[0])
        maxSum = -math.inf

        for i, sums in enumerate(dp):
            if sums[0] == -1:
                continue
            eligible_M = dp[:i - L + 1] + dp[i + M:]
            # print (sums[0], eligible_M, max(eligible_M, key=lambda x: x[1])[1])
            maxSum = max(maxSum, sums[0] + max(eligible_M, key=lambda x: x[1])[1])

        # print(maxSum)
        # print(dp)
        return maxSum
