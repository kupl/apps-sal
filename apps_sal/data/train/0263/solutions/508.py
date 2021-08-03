class Solution:
    def nextPositions(self, n):
        x, y = self.x_y_map[n]
        arr = [(x - 2, y + 1), (x - 1, y + 2), (x + 1, y + 2), (x + 2, y + 1), (x + 2, y - 1), (x + 1, y - 2), (x - 1, y - 2), (x - 2, y - 1)]
        return [self.reverse_map[v] for v in arr if v in self.reverse_map]

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
        self.x_y_map = self.build_x_y_map()
        self.reverse_map = {v: k for k, v in list(self.x_y_map.items())}

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
