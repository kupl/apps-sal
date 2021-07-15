from functools import lru_cache

class Solution:
    def knightDialer(self, N: int) -> int:
        @lru_cache(None)
        def _jump(row, col, remaining):
            if remaining == 1:
                return 1
            total = 0
            for dr, dc in (2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2):
                if (
                    0 <= row + dr < m and 0 <= col + dc < n and pad[row + dr][col + dc]
                ):
                    total += _jump(row + dr, col + dc, remaining - 1)
            return total % MAX

        MAX = 10**9 + 7
        pad = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
            [0, 1, 0]
        ]
        m, n = len(pad), len(pad[0])
        total = 0
        for i in range(m):
            for j in range(n):
                if pad[i][j]:
                    total += _jump(i, j, N)
        return total % MAX
