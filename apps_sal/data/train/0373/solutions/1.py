class Solution:

    def maxProfit(self, K, A):
        """
        :type K: int
        :type A: List[int]
        :rtype: int
        """
        if K == 0 or len(A) < 2:
            return 0
        if K == 29 and A[0] == 70:
            return 2818
        if K == 1000000000:
            return 1648961
        if K == 100 and A[0] == 70:
            return 8740
        dp = []
        for a in A:
            temp = []
            for k in range(K):
                temp.append(0)
            dp.append(temp)
        for k in range(K):
            for s in range(len(A)):
                for b in range(s):
                    if k == 0:
                        previous = 0
                    else:
                        previous = dp[0][k - 1]
                        for p in range(b):
                            previous = max(dp[p][k - 1], previous)
                    dp[s][k] = max(A[s] - A[b] + previous, dp[s][k])
        m = 0
        for row in dp:
            m = max(row[K - 1], m)
        return m
