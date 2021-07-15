class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        length = len(stoneValue)

        # dp[i] denote sum of items selected by Alice subtract sum of Bob from i to last
        dp = {}
        kA = 'Alice'
        kB = 'Bob'
        for index in range(length-1, -1, -1):
            minus = length - index
            rA = rB = 0
            if minus >= 3:  # normal case >=3; three choices
                # choice 1: select all the three
                c1 = stoneValue[index] + stoneValue[index + 1] + stoneValue[index + 2]

                # choice 2: select first two
                c2 = stoneValue[index] + stoneValue[index + 1]

                # choice 3: select first one
                c3 = stoneValue[index]

                # Alice
                rA = max(c1 + dp.get((index + 3, kB), 0), c2 + dp.get((index + 2, kB), 0),
                         c3 + dp.get((index + 1, kB), 0))

                # Bob
                rB = min(-c1 + dp.get((index + 3, kA), 0), -c2 + dp.get((index + 2, kA), 0),
                         -c3 + dp.get((index + 1, kA), 0))
            elif minus == 2:  # remain two, two choices
                # choice 1: select all the two
                c1 = stoneValue[index] + stoneValue[index + 1]

                # choice 2: select the first of the two
                c2 = stoneValue[index]

                # Alice select
                rA = max(c1, c2 + dp.get((index + 1, kB), 0))

                # Bob select
                rB = min(-c1, -c2 + dp.get((index + 1, kA), 0))
            elif minus == 1:  # remain one, only one choice
                c1 = stoneValue[index]
                rA = c1
                rB = -c1

            dp[(index, kA)] = rA
            dp[(index, kB)] = rB

        #print(stoneValue)
        #print(dp)
        result = dp.get((0, kA))
        if result > 0:
            return 'Alice'
        elif result < 0:
            return 'Bob'
        else:
            return 'Tie'
