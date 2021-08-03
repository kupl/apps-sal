class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 1:
            return 10
        next_square = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [0, 1, 7], [2, 6], [1, 3], [2, 4], [4, 6]]

        values = [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
        for i in range(1, n):
            next_values = [0] * 10
            for num in range(10):
                for square in next_square[num]:

                    next_values[square] %= MOD
                    next_values[square] += values[num]

            values = next_values[:]

        return sum(values) % MOD
