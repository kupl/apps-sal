class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        MOD = (10 ** 9) + 7
        # print(MOD)
        
        f = min(f, target)
        
        dp = [[0 for t in range(target + 1)] for r in range(d)]
        
        # initialize for first roll (using just one die)
        for i in range(1, f+1):
            dp[0][i] = 1
        
        
        # with dp, number of states can be 1 - 1000
        
        # how many ways can I get from a to b in less than 7 rolls?
        # how many ways can I get from 0 to target in less than d rolls?
        
        # with transition cost as # of dice: 
        
        # fill table
        # simulate number of ways using 2 dice, then 3, etc.
        for r in range(1, d):
            # for each possible running sum
            for i in range(1, target + 1):
                # check if this sum is reachable by some roll of the new die
                for val in range(1, f+1):
                    if i-val >= 0:
                        # add the number of ways to get to the current sum from the
                        # previous sum, use modulus at this point to reduce computation costs
                        dp[r][i] = (dp[r-1][i-val] + dp[r][i]) % MOD

        # return the number of ways to reach target, using ALL dice
        return dp[-1][target]
        
        

