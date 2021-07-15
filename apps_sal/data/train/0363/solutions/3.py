class Solution:
    def dfs(self, A, i, j):
        if i<0 or j<0 or i>=len(A) or j>=len(A[i]):
            return
        
        if A[i][j] == 0:
            return
        
        A[i][j] = 0
        self.dfs(A, i+1, j)
        self.dfs(A, i-1, j)
        self.dfs(A, i, j+1)
        self.dfs(A, i, j-1)
        
    def numEnclaves(self, A: List[List[int]]) -> int:
        if not A:
            return
        
        for row in range(len(A)):
            for col in range(len(A[row])):
                    if row == 0 or row == len(A)-1 or col == 0 or col == len(A[row]) - 1 and A[row][col] == 1:
                        self.dfs(A, row, col)
        
        count = 0
        for row in range(len(A)):
            for col in range(len(A[row])):
                if A[row][col] == 1:
                    count+=1
        
        return count

