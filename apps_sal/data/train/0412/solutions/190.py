class Solution:
    """
    DP formula:
    calc(d, target) = calc(d-1, target - 1) + calc(d-1, target - 2) + ... + calc(d-1, target - f)
    example:
    d = 2, target = 7, f = 6
    calc(1, 1) = 1  -> one way to get 1 out of one 6 faced dice
    calc(1, 2) = 1  -> one way to get 2 out of one 6 faced dice
    calc(1, 3) = 1  -> one way to get 3 out of one 6 faced dice
    ...
    calc(1, 6) = 1 -> one way to get 6 out of one 6 faced dice
    calc(1, 7) = 0 -> NO way to get 7 from one 6 faced dice
    similarly, no way to get value > f using just one dice

    calc(2, 1) = 0 -> 2 dice, target 1. impossible to get 1 using 2 six faced dice.
    calc(2, 2) = 1 -> calc(1, 1) = 1. ways getting 2 out of 2 dice is similar to getting 1 out of 1 dice
    calc(2, 3) = calc(1, 2) + calc(1, 1) = 1 + 1 = 2
                 ways of getting 3 out of 2 dice meaning, ways of getting 2 using one dice [calc(1, 2)] 
                 and getting 1 from other dice [calc(1, 1)]
    calc(2, 6) = calc(1, 1) + calc(1, 2) + calc(1, 3) + calc(1, 4) + calc(1, 5) + calc(1, 6)
                ways to get 1 out of 1 dice then getting 5 from second dice +
                ways to get 2 from first dice and then getting 4 from second dice +
                ways to get 3 from first dice and getting 3 from second dice +
                ways to get 4 from first dice and getting 2 from second dice +
                ways to get 5 from first dice and getting 1 from second dice
    """

    def numRollsToTarget(self, d, f, target):
        mod_v = 10 ** 9 + 7
        dp = [[0] * (target + 1) for _ in range(d + 1)]
        for i in range(1, f + 1):
            if i > target:
                break
            dp[1][i] = 1
        for i in range(2, d + 1):
            for j in range(i, target + 1):
                for k in range(1, f + 1):
                    if j - k >= 0:
                        dp[i][j] += dp[i - 1][j - k]
                        dp[i][j] %= mod_v
                    else:
                        break
        return dp[d][target]
