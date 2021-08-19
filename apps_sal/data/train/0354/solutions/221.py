class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        def rec(die, cons, empty):
            if empty == 0:
                return 1

            ans = 0
            if (die, cons, empty) in dp:
                return dp[(die, cons, empty)]
            for r in range(6):
                if r != die:
                    ans += rec(r, 1, empty - 1)
                elif cons < rollMax[die]:
                    ans += rec(die, cons + 1, empty - 1)
            dp[(die, cons, empty)] = ans
            return ans
        dp = {}
        return rec(0, 0, n) % (10 ** 9 + 7)


# class Solution:
#     def dieSimulator(self, n: int, rollMax: List[int]) -> int:
#         def f(n, num, co):

#             if n == 0:
#                 return 1

#             if (n, num, co) in dp:
#                 return dp[n, num, co]

#             ans = 0
#             for i in range(1, 7):
#                 if i == num and co + 1 <= rollMax[i - 1]:
#                     ans += f(n - 1, i, co + 1)
#                 else:
#                     ans += f(n - 1, i, 1)
#             dp[n, num, co] = ans
#             return ans

#         dp = {}
#         return f(n, 0, 0) % (10 ** 9 + 7)
