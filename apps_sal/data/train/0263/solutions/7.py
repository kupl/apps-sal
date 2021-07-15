class Solution:
    def knightDialer(self, n: int) -> int:
        moves = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [0, 3, 9],
            [],
            [0, 1, 7],
            [2, 6],
            [1, 3],
            [2, 4],
        ]
        kmod = 10**9 + 7
        dp = [1] * 10
        for k in range(1, n):
            tmp = [0] * 10
            for i in range(10):
                for j in moves[i]:
                    tmp[j] = (tmp[j] + dp[i]) % kmod
            dp = tmp
        res = 0
        for i in range(10):
            res = (res + dp[i]) % kmod
        return res
