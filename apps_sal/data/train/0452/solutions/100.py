class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # 0928
        # dp(i,k)=到jobDifficulty[i]为止的job（共i+1个），使用k天完成的 minimum difficulty
        if len(jobDifficulty) < d:
            return -1
        dp = [[10000] * (d + 1) for i in range(len(jobDifficulty))]
        dp[0][1] = jobDifficulty[0]
        for i in range(len(jobDifficulty)):
            for k in range(1, d + 1):
                # print(\"i,\",i,\"k,\",k)
                if k == 1:
                    dp[i][k] = max(jobDifficulty[:i + 1])
                    continue
                if k > i + 1 or (i == 0 and k == 1):
                    # print(\"continue\")
                    continue
                mind = 10000
                for j in range(0, i):
                    # print(\"j=\",j,dp[j][k-1])
                    mind = min(dp[j][k - 1] + max(jobDifficulty[j + 1:i + 1]), mind)
                    # print(\"mind\",mind)
                dp[i][k] = mind
        print(dp)
        return dp[-1][-1]
