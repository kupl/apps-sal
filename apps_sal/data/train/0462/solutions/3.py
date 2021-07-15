class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        for i,row in enumerate(grid):
            if row.count(1)>1:
                for j,val in enumerate(row):
                    if val==1:
                        grid[i][j]=2
        for j,col in enumerate(zip(*grid)):
            if col.count(1)+col.count(2)>1:
                for i,val in enumerate(col):
                    if val==1:
                        grid[i][j]=2
        return sum(1 for row in grid for val in row if val==2)

