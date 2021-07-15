class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        faces = len(rollMax)
        # [n + 1][faces + 1] dimensional dp array
        dp = [[0 for i in range(faces + 1)] for j in range(n + 1)]
        
        # initialization
        # roll 0 times, the total combination is 1
        dp[0][faces] = 1
        # roll 1 times, the combinations that end at face j is 1
        for j in range(faces):
            dp[1][j] = 1
        # roll 1 times, the total combination is faces = 6
        dp[1][faces] = faces
        
        # then roll dices from 2 times, until n times
        for i in range(2, n + 1):
            # iterate through each column (face)
            for j in range(faces):
                # at each [i, j], trying to go up (decrease i) and collect all the sum of previous state
                k = 1
                while i - k >= 0 and k <= rollMax[j]:
                    dp[i][j] += dp[i - k][faces] - dp[i - k][j]
                    k+=1
            # update total sum of this row
            dp[i][faces] = sum(dp[i])
        
        return dp[n][faces] % 1000000007
        
        
                

