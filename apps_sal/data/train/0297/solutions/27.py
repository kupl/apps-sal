class Solution:
    def get_permute(self, opts, cur_sol):
        for i in range(len(opts)):
            c = opts[i]
            cur_sol.append(c)
            self.solutions.add(''.join(cur_sol))
            opts2 = opts
            opts2 = opts2[:i] + opts2[i + 1:]
            self.get_permute(opts2, cur_sol)
            cur_sol.pop()

    def numTilePossibilities(self, tiles: str) -> int:
        self.solutions = set()
        self.get_permute(tiles, [])
        return len(self.solutions)
