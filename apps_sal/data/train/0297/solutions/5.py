class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        pos = set()

        def choose(s, n, pref=''):
            if n == 0:
                pos.add(pref)

            for i in range(len(s)):
                choose(s[:i] + s[i + 1:], n - 1, pref + s[i])

        for i in range(1, len(tiles) + 1):
            choose(tiles, i)
        return len(pos)
