class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        result = set()
        vis = [0] * len(tiles)

        def dfs(res, depth):
            if res:
                result.add(res)
            if depth == len(tiles) - 1:
                result.add(res)
            for i in range(len(tiles)):
                if not vis[i]:
                    vis[i] = 1
                    dfs(res + tiles[i], depth + 1)
                    vis[i] = 0
        dfs('', -1)
        return len(result)
