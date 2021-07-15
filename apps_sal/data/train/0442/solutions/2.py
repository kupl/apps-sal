class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            j = len(grid[i]) - 1
            while j >= 0 and grid[i][j] == 0:
                j -= 1
            grid[i] = j
            
        count = 0
        
        for i in range(len(grid)):
            if grid[i] <= i:
                continue
            j = i + 1
            while j < len(grid) and grid[j] > i:
                j += 1
            if j == len(grid):
                return -1
            while j > i:
                grid[j], grid[j - 1] = grid[j - 1], grid[j]
                count += 1
                j -= 1
        return count
