MODULE = 10 ** 9 + 7


class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        MOVEMENTS = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        dp = [2, 2, 2, 2, 3, 0, 3, 2, 2, 2]
        for idx in range(2, n):
            new_dp = [0] * 10
            for jdx in range(10):
                for next_jdx in MOVEMENTS[jdx]:
                    new_dp[next_jdx] += dp[jdx]
            dp = new_dp

        print(dp)
        return sum(dp) % MODULE

