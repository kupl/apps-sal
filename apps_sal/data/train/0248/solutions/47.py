class Solution:

    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        class roots:

            def __init__(self, val):
                self.val = val
                self.par = None

            def root(self):
                if self.par == None:
                    return self.val
                return self.par.root()
        chains = {}
        for i in range(m):
            for j in range(n):
                if i > 0 and grid[i - 1][j] == grid[i][j]:
                    chains[i, j] = roots((i, j))
                    chains[i, j].par = chains[i - 1, j]
                if j > 0 and grid[i][j - 1] == grid[i][j]:
                    if (i, j) in chains:
                        if chains[i, j].root() == chains[i, j - 1].root():
                            return True
                        else:
                            chains[chains[i, j - 1].root()].par = chains[i, j]
                    else:
                        chains[i, j] = roots((i, j))
                        chains[i, j].par = chains[i, j - 1]
                if (i, j) not in chains:
                    chains[i, j] = roots((i, j))
        return False
