from functools import lru_cache


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = {}

        def roll(value, consecutiveRolls, left):
            if left == 0:
                return 1

            if (value, consecutiveRolls, left) in dp:
                return dp[value, consecutiveRolls, left]
            #print(value, consecutiveRolls, left)
            # if dp[value][consecutiveRolls][left] != -1:
            #    return dp[value][consecutiveRolls][left]

            rolls = 0
            for i in range(6):
                if i != value:
                    rolls += roll(i, 1, left - 1)
                else:
                    if consecutiveRolls < rollMax[i]:
                        rolls += roll(i, consecutiveRolls + 1, left - 1)

            dp[value, consecutiveRolls, left] = rolls

            return rolls

        return roll(0, 0, n) % (10**9 + 7)
