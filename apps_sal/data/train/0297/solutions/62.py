from collections import Counter


class Solution:

    def numTilePossibilities(self, tiles: str) -> int:

        def permutation(num, tiles_counter):
            if num == 1:
                return len(list(tiles_counter))
            rs = 0
            for c in +tiles_counter:
                rs += permutation(num - 1, tiles_counter - Counter({c: 1}))
            return rs
        total = 0
        for i in range(1, len(tiles) + 1):
            total += permutation(i, Counter(tiles))
        return total
