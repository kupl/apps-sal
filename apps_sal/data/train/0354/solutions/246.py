from functools import lru_cache


class Solution:
    def dieSimulator(self, n, roll_max):

        dicti = {}

        def dp(roll, last, count):
            if not roll:
                return 1
            elif (roll, last, count) in dicti:
                return dicti[roll, last, count]

            ans = 0
            for i in range(6):
                if i != last:
                    ans += dp(roll - 1, i, 1)
                elif count < roll_max[i]:
                    ans += dp(roll - 1, last, count + 1)
            dicti[roll, last, count] = ans % (10**9 + 7)
            return dicti[roll, last, count]
        return dp(n, -1, 0)
