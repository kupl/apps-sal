class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        '''
        for j = 0, 1, ..., faces - 1
        dp[i][j] means how many combinations it could be that at i-th rolling and the last face is j
        for j = faces
        dp[i][j] means how many combinations in total with i rollings
        
        '''
        faces = len(rollMax)
        # [n+1][faces+1] dimensional dp array
        dp = [[0 for _ in range(faces+1)] for _ in range(n+1)]
        
        #initialization
        # roll 0 times, the total combination is 1
        dp[0][faces] = 1
        # roll 1 times, the combinations that end at face j is 1
        for j in range(faces):
            dp[1][j] = 1
        # roll 1 times, the total combination is faces = 6
        dp[1][faces] = faces
        
        # then roll dices from 2 times, until n times
        for i in range(2, n+1):
            # iterate thru each face
            for j in range(faces):
                # at each [i, j], trying to go up (decrease i) and collect all the sum of previous state
                for k in range(1, rollMax[j]+1):
                    if i-k < 0:
                        break
                    # give me all the combinations as long as the last face is not j
                    dp[i][j] += dp[i-k][faces] - dp[i-k][j]
            dp[i][faces] = sum(dp[i])
        return dp[n][faces] % 1000000007
