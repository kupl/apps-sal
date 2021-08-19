class Solution:

    def knightDialer(self, n: int) -> int:
        movements = {0: (4, 6), 1: (6, 8), 2: (7, 9), 3: (4, 8), 4: (0, 3, 9), 5: (), 6: (0, 1, 7), 7: (2, 6), 8: (1, 3), 9: (2, 4)}
        total = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        for _ in range(n - 1):
            curr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for num in range(10):
                for move in movements[num]:
                    curr[move] = (curr[move] + total[num]) % (10 ** 9 + 7)
            total = curr
        return sum(total) % (10 ** 9 + 7)
