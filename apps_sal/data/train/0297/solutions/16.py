class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        setter = set()
        res = []
        for r in range(1, len(tiles) + 1):
            res.append(list(itertools.permutations(tiles, r)))
        result = []
        for re in res:
            result.append(list(set(re)))
        leng = 0
        for i in result:
            leng += len(i)
        return leng
