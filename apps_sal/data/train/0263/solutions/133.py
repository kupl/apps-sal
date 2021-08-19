class Solution:
    neighbors = {1: (6, 8), 2: (7, 9), 3: (4, 8), 4: (3, 9, 0), 5: tuple(), 6: (1, 7, 0), 7: (2, 6), 8: (1, 3), 9: (2, 4), 0: (4, 6)}

    def knightDialer(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 10
        prev_moves = [1] * 10
        current_moves = [0] * 10
        for i in range(n - 1):
            for j in range(10):
                current_moves[j] = sum((prev_moves[k] for k in self.neighbors[j])) % (10 ** 9 + 7)
            prev_moves = current_moves[:]
        return sum(prev_moves) % (10 ** 9 + 7)
