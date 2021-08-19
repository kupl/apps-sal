class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        res = {}

        def dfs(seq, tiles):
            if seq not in res and seq != '':
                res[seq] = 1
            for i in range(len(tiles)):
                dfs(seq + tiles[i], tiles[:i] + tiles[i + 1:])
        dfs('', tiles)
        return len(res)
