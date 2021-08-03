from itertools import permutations


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        total = 0
        for size in range(1, len(tiles) + 1):
            total += len(set(permutations(tiles, size)))

        return total
