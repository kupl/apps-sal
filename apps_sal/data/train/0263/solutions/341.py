class Solution:

    def _knightDialer(self, n: int, curr_n: int, moves_map: dict, cache: dict) -> int:
        if n == 0:
            return 1
        if (curr_n, n) in cache:
            return cache[curr_n, n]
        distinct_nums = 0
        for next_n in moves_map[curr_n]:
            distinct_nums += self._knightDialer(n - 1, next_n, moves_map, cache)
        cache[curr_n, n] = distinct_nums
        return cache[curr_n, n]

    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        mod = 10 ** 9 + 7
        nums = 0
        cache = {}
        moves_map = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        nums = 0
        for (m, weight) in [(1, 4), (2, 2), (4, 2), (0, 1)]:
            nums += weight * self._knightDialer(n - 1, m, moves_map, cache)
        return nums % mod
