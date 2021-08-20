class Solution:

    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n == 1:
            return 10
        neighbors = {0: (4, 6), 1: (6, 8), 2: (7, 9), 3: (8, 4), 4: (3, 9, 0), 5: tuple(), 6: (7, 1, 0), 7: (2, 6), 8: (1, 3), 9: (4, 2)}
        prev_jump = [1] * 10
        curr_jump = [0] * 10
        jump = 0
        for jump in range(0, n - 1):
            curr_jump = [0] * 10
            for num in range(0, 10):
                for i in neighbors[num]:
                    curr_jump[i] += prev_jump[num]
                    curr_jump[i] %= MOD
            prev_jump = curr_jump
        return sum(curr_jump) % MOD
