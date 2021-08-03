class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        res = set()

        def backtrack(path, curr):
            if path not in res:
                if path:
                    res.add(path)
                for i in range(len(curr)):
                    backtrack(path + curr[i], curr[:i] + curr[i + 1:])

        backtrack('', tiles)
        return len(res)
