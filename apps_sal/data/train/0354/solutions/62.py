class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        memo = [[0] * 6 for _ in range(n)]
        for i in range(n):
            for x in range(6):
                maxRolls = rollMax[x]
                for j in range(i - 1, i - 1 - maxRolls, -1):
                    if j == -1:
                        memo[i][x] += 1
                        break

                    for y in range(6):
                        if y != x:
                            memo[i][x] += memo[j][y]

        return sum(memo[-1]) % (10 ** 9 + 7)
