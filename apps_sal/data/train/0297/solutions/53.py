from itertools import combinations as C
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        num = 0
        for i in range(1, len(tiles)+1):
            l = set(permutations(tiles, i))
            num += len(l)
        return num
