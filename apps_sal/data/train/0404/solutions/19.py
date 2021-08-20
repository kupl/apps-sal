class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:

        def ave(list_):
            return sum(list_) / len(list_)
        dp = {}

        def rec(index, k):
            if index == len(A):
                return 0
            if (index, k) in dp:
                return dp[index, k]
            if k == 1:
                return ave(A[index:])
            m = 0
            for i in range(index + 1, len(A)):
                m = max(m, ave(A[index:i]) + rec(i, k - 1))
            dp[index, k] = m
            return m
        return rec(0, K)
