class Solution:
    def knightDialer(self, n: int) -> int:
        mod_num = 10 ** 9 + 7
        moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]
        cells = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 1)]
        cell2idx = {}
        for i, cell in enumerate(cells):
            cell2idx[cell] = i
        sequences = [1 for _ in cells]
        for step in range(n - 1):
            new_sequences = [0 for _ in cells]
            for i, (r, c) in enumerate(cells):
                for rm, cm in moves:
                    newr = r + rm
                    newc = c + cm
                    if (newr, newc) in cell2idx:
                        new_idx = cell2idx[(newr, newc)]
                        new_sequences[new_idx] += sequences[i]
            sequences = [cnt % mod_num for cnt in new_sequences]
        return sum(sequences) % mod_num
