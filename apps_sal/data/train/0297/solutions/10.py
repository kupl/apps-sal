
class Solution:
    def __init__(self):
        self.seen = set()
        self.result = set()

    def numTilePossibilities(self, tiles: str) -> int:
        self.dfs(tiles, 0, [])
        return len(self.result) - 1

    def dfs(self, string, idx, path):
        
        st = ''.join(path)

        if st not in self.seen:
            self.result.update((''.join(p) for p in permutations(st)))
            self.seen.add(st)
        
        for i in range(idx, len(string)):
            self.dfs(string, i + 1, path + [string[i]])
