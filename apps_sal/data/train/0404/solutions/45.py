class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        p = [0]
        for i in range(n):
            p.append(p[i]+A[i])
        def average(i,j):
            return (p[j]-p[i]) / (j-i)
        dp = [[0]*n for _ in range(K)]
        for i in range(n):
            dp[0][i] = average(i,n)            
            

        for k in range(1, K):
            for i in range(n):
                for j in range(i+1, n):
                    dp[k][i] = max(dp[k][i], average(i,j)+dp[k-1][j])
        return dp[K-1][0]
