class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        d = set()
        for i in range(len(tiles)):
            for x in list(permutations(tiles, i + 1)):
                d.add(''.join(x))
        print(d)
        return len(d)
