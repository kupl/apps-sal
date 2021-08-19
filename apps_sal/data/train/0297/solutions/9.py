class Solution:

    def numTilePossibilities(self, tiles: str) -> int:

        def count(tiles):
            counter = set()
            if len(tiles) == 1:
                counter.add(tiles)
            elif len(tiles) == 2:
                counter.add(tiles)
                counter.add(tiles[::-1])
                counter.add(tiles[0])
                counter.add(tiles[1])
            else:
                for (idx, i) in enumerate(tiles):
                    x = count(tiles[:idx] + tiles[idx + 1:])
                    extra = set()
                    for j in x:
                        extra.add(tiles[idx] + j)
                        extra.add(j + tiles[idx])
                        for k in range(1, len(j) - 1):
                            extra.add(j[:k] + tiles[idx] + j[k + 1:])
                    x.update(extra)
                    counter.update(x)
            return counter
        return len(count(tiles))
