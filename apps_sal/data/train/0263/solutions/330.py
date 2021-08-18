class Solution:
    def knightDialer(self, n: int) -> int:
        modulo = 10**9 + 7

        dp = [1] * 10

        while n > 1:
            new_table = [0] * 10
            for digit in range(0, 10):
                for neighbor in self.neighbors(digit):
                    new_table[neighbor] += dp[digit]
            n -= 1
            dp = new_table

        return sum(dp) % modulo

    def neighbors(self, digit):
        neighbors = {
            0: (4, 6),
            1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (0, 3, 9),
            5: (),
            6: (0, 1, 7),
            7: (2, 6),
            8: (1, 3),
            9: (2, 4)

        }

        return neighbors[digit]
