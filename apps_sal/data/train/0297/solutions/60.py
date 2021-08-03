class Solution:
    memos = dict()

    def numTilePossibilities(self, tiles: str) -> int:
        tiles = ''.join(sorted(tiles))
        uniques = self.step(tiles)
        return len(uniques) - 1

    def step(self, tiles: str) -> set:
        if len(tiles) == 0:
            return {''}
        if tiles not in self.memos:
            uniques = set()
            for i in range(len(tiles)):
                c = tiles[i]
                substr = tiles[:i] + tiles[i + 1:]
                substrs_set = self.step(substr)
                for substr in substrs_set:
                    uniques.add(substr)
                    for j in range(len(substr) + 1):
                        new_str = substr[:j] + c + substr[j:]
                        uniques.add(new_str)
            self.memos[tiles] = uniques
        return self.memos[tiles]
