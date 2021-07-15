NEIGHBORS_MAP = {
    1: (6, 8),
    2: (7, 9),
    3: (4, 8),
    4: (3, 9, 0),
    5: tuple(),  # 5 has no neighbors
    6: (1, 7, 0),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
    0: (4, 6),
}


def neighbors(position):
    return NEIGHBORS_MAP[position]


class Solution:
    def knightDialer(self, num_hops):
        cache = {}
        mod = 10**9 + 7

        def helper(position, num_hops):
            if (position, num_hops) in cache:
                return cache[(position, num_hops)]
            if num_hops == 0 or num_hops == 1:
                return 1
            num_sequences = 0
            for neighbor in neighbors(position):
                num_sequences += helper(neighbor, num_hops - 1)
            cache[(position, num_hops)] = num_sequences
            # print(cache)
            return num_sequences

        res = 0
        for i in range(0, 10):
            res += helper(i, num_hops)
        # print(res, cache)
        return res % mod

