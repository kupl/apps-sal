class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()

        def seq(s, l):
            if len(l) == 0:
                res.add(s)
                return
            seq(s, l[1:])
            for i in range(len(l)):
                seq(s + l[i], l[: i] + l[i + 1:])

        seq('', list(tiles))

        return len(res) - 1
