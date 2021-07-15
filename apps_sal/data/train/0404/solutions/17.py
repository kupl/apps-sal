# dp[i][k] = largest sum of avg for A[:(i+1)] splitted into most k groups
# = max{max[dp[j][k-1]+avg(A[(j+1):(i+1)]) for j<i], dp[i][k-1]}
class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        import itertools
        cumsum = list(itertools.accumulate(A)) #if use mean, over time limit
#         print(\"cumsum\", cumsum)
        L = len(A)
        K = min(L, K)
        dp = [[0]*(K+1) for i in range(L)]
        for i in range(L):
            dp[i][1] = (cumsum[i])/(i+1) # we don't use dp[i][0]
        for k in range(2,K+1):
            for i in range(L):
                tmp = dp[i][k-1]
                for j in range(i):
                    tmp = max(tmp, dp[j][k-1]+(cumsum[i]-cumsum[j])/(i-j))
                dp[i][k] = tmp
#         print(dp)
        return dp[-1][K]         
