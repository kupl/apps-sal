class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        length = len(stoneValue)
        dp = {}
        kA = 'Alice'
        kB = 'Bob'
        for index in range(length - 1, -1, -1):
            minus = length - index
            rA = rB = 0
            if minus >= 3:
                c1 = stoneValue[index] + stoneValue[index + 1] + stoneValue[index + 2]
                c2 = stoneValue[index] + stoneValue[index + 1]
                c3 = stoneValue[index]
                rA = max(c1 + dp.get((index + 3, kB), 0), c2 + dp.get((index + 2, kB), 0), c3 + dp.get((index + 1, kB), 0))
                rB = min(-c1 + dp.get((index + 3, kA), 0), -c2 + dp.get((index + 2, kA), 0), -c3 + dp.get((index + 1, kA), 0))
            elif minus == 2:
                c1 = stoneValue[index] + stoneValue[index + 1]
                c2 = stoneValue[index]
                rA = max(c1, c2 + dp.get((index + 1, kB), 0))
                rB = min(-c1, -c2 + dp.get((index + 1, kA), 0))
            elif minus == 1:
                c1 = stoneValue[index]
                rA = c1
                rB = -c1
            dp[index, kA] = rA
            dp[index, kB] = rB
        result = dp.get((0, kA))
        if result > 0:
            return 'Alice'
        elif result < 0:
            return 'Bob'
        else:
            return 'Tie'
