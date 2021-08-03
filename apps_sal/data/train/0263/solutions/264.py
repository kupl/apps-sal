from collections import defaultdict
move_map = {
    0: {4, 6},
    1: {6, 8},
    2: {7, 9},
    3: {4, 8},
    4: {3, 9, 0},
    5: {},
    6: {1, 0, 7},
    7: {2, 6},
    8: {1, 3},
    9: {2, 4}
}


class Solution:
    def knightDialer(self, n: int) -> int:
        table = defaultdict(int)
        for key in move_map:
            table[key, 1] = 1

        for N in range(2, n + 1):
            for key in move_map:
                for new_key in move_map[key]:
                    table[key, N] += table[new_key, N - 1]

        res = 0
        for key in move_map:
            res += table[key, n]
        return res % (10**9 + 7)
