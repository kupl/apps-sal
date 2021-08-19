class Solution:

    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        (dp, counts) = ([0, 0], 1)
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp.append(dp[i - 1] + counts)
                counts += 1
            else:
                dp.append(dp[i - 1])
                counts = 1
        return dp[-1]
