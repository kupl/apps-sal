class Solution:

    def knightDialer(self, n: int) -> int:
        moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        previous = {(r, c): 1 for (r, c) in ((0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 1))}
        current = {(r, c): 0 for (r, c) in previous}
        for i in range(n - 1):
            for ((r, c), v) in previous.items():
                for (dr, dc) in moves:
                    if (r + dr, c + dc) in current:
                        current[r + dr, c + dc] += v
                        current[r + dr, c + dc] %= 1000000007
            previous = current
            current = {(r, c): 0 for (r, c) in previous}
        return sum(previous.values()) % 1000000007
