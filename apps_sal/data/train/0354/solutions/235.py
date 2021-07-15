class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        m = max(rollMax)
        dp = [[1]+[0]*(m-1) for _ in range(len(rollMax))]
        MOD = 1e9+7
        for i in range(1, n):
            tempSumPrev = [0]*len(rollMax)
            tempDp = [[0]*m for _ in range(len(rollMax))]
            totalSumPrev = 0
            for p in dp:
                for q in p:
                    totalSumPrev = (totalSumPrev+q)%MOD
            for j in range(len(rollMax)):
                tempDp[j][0] = totalSumPrev-sum(dp[j])
                for k in range(1, rollMax[j]):
                    tempDp[j][k] = dp[j][k-1]
            dp = tempDp
        return int(sum(q for p in dp for q in p)%MOD)
