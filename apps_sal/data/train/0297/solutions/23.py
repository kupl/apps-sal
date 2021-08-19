class Solution:

    def numTilePossibilities(self, tiles: str) -> int:

        def dfs(path, t):
            if path:
                result.add(path)
            for i in range(len(t)):
                dfs(path + t[i], t[:i] + t[i + 1:])
        result = set()
        dfs('', tiles)
        return len(result)
