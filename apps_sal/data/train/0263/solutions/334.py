NEIGHBORS_MAP = {
    1: (6, 8),
    2: (7, 9),
    3: (4, 8),
    4: (3, 9, 0),
    5: tuple(),
    6: (1, 7, 0),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
    0: (4, 6),
}


class Solution:
    def nextPositions(self, n):
        return NEIGHBORS_MAP[n]

    def build_x_y_map(self):
        r, c = 0, 0
        ht = {}

        for i in range(1, 10):
            ht[i] = (r, c)
            c += 1
            if c == 3:
                r += 1
                c = 0

        ht[0] = (3, 1)
        return ht

    def knightDialer(self, n: int) -> int:
        def count_moves(curr_cell, hops, memo):
            if hops == 0:
                return 1
            key = (curr_cell, hops)
            if key not in memo:
                ways = 0
                for pos in self.nextPositions(curr_cell):
                    ways += count_moves(pos, hops - 1, memo)
                memo[key] = ways
            return memo[key]

        total = 0
        memo = {}
        for i in range(0, 10):
            total += count_moves(i, n - 1, memo)
        return total % (10**9 + 7)
