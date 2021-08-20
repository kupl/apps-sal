class Solution:

    def numTilePossibilities(self, tiles: str) -> int:

        def perm(k, a):
            if k == 0:
                return []
            elif k == 1:
                return [x for x in a]
            else:
                return [a[i] + y for i in range(len(a)) for y in perm(k - 1, a[:i] + a[i + 1:])]
        out = set()
        for i in range(1, len(tiles) + 1):
            for x in perm(i, tiles):
                out.add(x)
        return len(out)
