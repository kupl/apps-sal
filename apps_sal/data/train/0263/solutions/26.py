class Solution:

    def knightDialer(self, n: int) -> int:
        total_jumps = [1] * 10
        neighbors = {0: (4, 6), 1: (6, 8), 2: (7, 9), 3: (4, 8), 4: (0, 3, 9), 5: (), 6: (0, 1, 7), 7: (2, 6), 8: (1, 3), 9: (2, 4)}
        for jumps_left in range(n - 1):
            next_jumps = [0] * 10
            for num in range(0, 10):
                for next_num in neighbors[num]:
                    next_jumps[next_num] = next_jumps[next_num] + total_jumps[num] % (10 ** 9 + 7)
            total_jumps = next_jumps
        return sum(total_jumps) % (10 ** 9 + 7)
