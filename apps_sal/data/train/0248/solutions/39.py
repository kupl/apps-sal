class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        '''
        [[\"a\",\"b\",\"b\"],
         [\"b\",\"z\",\"b\"],
         [\"b\",\"b\",\"a\"]]
        
        [[\"a\",\"b\",\"b\"],
         [\"b\",\"b\",\"b\"],
         [\"b\",\"b\",\"a\"]]
        
        dfs(pre_i,pre_j, i,j):-> bool: hasLoop
        '''
        label = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        def dfs(pre_i,pre_j, i,j):
            if label[i][j] == 1: # is being visited
                return True
            if label[i][j] == -1:# visited
                return False
            label[i][j] = 1
            for ii, jj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=ii<len(grid) and 0<=jj<len(grid[ii]):
                    if grid[ii][jj] == grid[i][j] and (not (ii==pre_i and jj==pre_j)):
                        if dfs(i,j,ii,jj): return True
            label[i][j] = -1
            return False
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if dfs(-1,-1, i,j): return True
        return False

