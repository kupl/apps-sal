class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        resset = set()
        
        for ri, row in enumerate(grid):
            tmp = [(ri, ci) for ci, cell in enumerate(row) if cell]
            
            if len(tmp) >= 2:
                resset.update(tmp)
        
        for ci, col in enumerate(zip(*grid)):
            # col = (row[ci] for row in grid)
            tmp = [(ri, ci) for ri, cell in enumerate(col) if cell]

            if len(tmp) >= 2:
                resset.update(tmp)
        
        return len(resset)

