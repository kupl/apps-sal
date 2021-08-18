class Solution:
    def dieSimulator(self, N: int, rollMax: List[int]) -> int:

        def dp(curr_cnt, curr, n):
            if curr > 0 and rollMax[curr - 1] < curr_cnt:
                return 0
            elif n == 0:
                return 1
            elif (curr_cnt, curr, n) in memo:
                return memo[(curr_cnt, curr, n)]
            else:
                res = 0
                for i in range(1, 7):
                    if i == curr:
                        res += dp(curr_cnt + 1, i, n - 1)
                    else:
                        res += dp(1, i, n - 1)
                memo[(curr_cnt, curr, n)] = res
                return res

        memo = dict()
        res = dp(0, 0, N)
        return res % (10**9 + 7)
