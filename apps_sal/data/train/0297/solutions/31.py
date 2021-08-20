class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        result = set()

        def dfs_helper(path, t):
            if path:
                result.add(path)
            for i in range(len(t)):
                dfs_helper(path + t[i], t[:i] + t[i + 1:])
        dfs_helper('', tiles)
        return len(result)
