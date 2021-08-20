class Solution:

    def knightDialer(self, n: int) -> int:
        path = [(4, 6), (6, 8), (7, 9), (4, 8), (0, 3, 9), (), (0, 1, 7), (2, 6), (1, 3), (2, 4)]
        memo = []
        for i in range(n + 1):
            memo.append({})
            for j in range(10):
                memo[i][j] = -1

        def dp(num, steps):
            if steps == 1:
                return 1
            if memo[steps][num] != -1:
                return memo[steps][num]
            ret = 0
            for i in path[num]:
                ret += dp(i, steps - 1)
            memo[steps][num] = ret
            return ret % 1000000007
        res = 0
        for num in range(10):
            res += dp(num, n)
            res %= 1000000007
        return res
