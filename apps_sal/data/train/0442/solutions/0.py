class Solution:

    def minSwaps(self, grid: List[List[int]]) -> int:
        start = 1
        swap = 0
        n = len(grid)
        zeros_ingrid = n - 1
        while zeros_ingrid > 0:
            swapped_grid = False
            for i in range(len(grid)):
                if sum(grid[i][start:]) == 0:
                    swap += i
                    grid.remove(grid[i])
                    swapped_grid = True
                    zeros_ingrid -= 1
                    start += 1
                    break
            if not swapped_grid:
                return -1
        return swap
