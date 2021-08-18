class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        rolls = []
        for i in range(d + 1):
            rolls.append([0] * (target + 1))

        for i in range(target + 1):
            rolls[0][i] = 0

        for i in range(d + 1):
            rolls[i][0] = 0

        for i in range(1, target + 1):
            if i <= f:
                rolls[1][i] = 1

        for i in range(2, d + 1):
            for j in range(1, target + 1):
                k = 1
                while(k <= f):
                    if(j - k) < 0:
                        break
                    rolls[i][j] += rolls[i - 1][j - k]
                    k += 1

        return (rolls[d][target] % (10**9 + 7))
