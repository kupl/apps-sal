class Solution(object):
    def largestSumOfAverages(self, A, K):
        prefix_sum = [0]
        for x in A:
            prefix_sum.append(prefix_sum[-1] + x)
        
        def average(i, j):
            return (prefix_sum[j] - prefix_sum[i]) / float(j - i)

        n = len(A)
        dp = [average(i, n) for i in range(n)]
        print(dp)
        
        for k in range(K-1):
            for i in range(n):
                for j in range(i+1, n):
                    dp[i] = max(dp[i], average(i, j) + dp[j])
        return dp[0]        
