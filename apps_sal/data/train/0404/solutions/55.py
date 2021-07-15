class Solution():
    def largestSumOfAverages(self, A, K: int) -> float:
        dp = []
        for i in range(len(A)):
            tmp = []
            for j in range(1, 1 + K):
                tmp.append(0)
            dp.append(tmp)
        v = 0
        for i in range(len(dp)):
            v += A[i]
            for j in range(len(dp[0])):
                if j == 0:
                    dp[i][j] = v / (i+1)
                elif j == i:
                    dp[i][j] = v
        for i in range(len(dp)):
            for j in range(1,min(i,K)):
                for t in range(i):
                    dp[i][j] = max(dp[i][j],dp[t][j-1]+self.avg(A[t+1:i+1]))
        return dp[-1][-1]

    def avg(self,nums):
        return sum(nums) / len(nums)

