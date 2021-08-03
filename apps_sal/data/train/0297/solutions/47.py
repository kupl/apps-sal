class Solution:
    def poss(self, tiles: str) -> set:
        if len(tiles) == 1:
            return set([tiles[0]])
        output = set()
        for i in range(len(tiles)):
            elem = tiles[i]
            res = self.poss(tiles[:i] + tiles[i + 1:])
            output = output.union(res)
            for elem in res:
                output.add(tiles[i] + elem)
        return output

    def numTilePossibilities(self, tiles: str) -> int:
        if len(tiles) == 0:
            return 0
        return len(self.poss(tiles))
