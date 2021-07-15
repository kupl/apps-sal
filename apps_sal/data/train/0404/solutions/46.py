class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        # dynamic programming, 
        avg = lambda arr: sum(arr) / len(arr)        
        n = len(A)
        dp = [[0] * K for _ in range(n)]
        for i in range(n):
            for k in range(K):
                if k == 0:
                    dp[i][k] = avg(A[:i+1])
                else:
                    if len(A[:i+1]) < k+1:
                        break
                    for j in range(i):
                        dp[i][k] = max(dp[j][k-1] + avg(A[j+1:i+1]), dp[i][k])
        print(dp)
        return dp[-1][-1]
