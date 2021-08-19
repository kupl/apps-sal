class Solution:

    def numEnclaves(self, A: List[List[int]]) -> int:

        def dfs(i, j):
            if not (0 <= i < len(A) and 0 <= j < len(A[i])):
                return
            if A[i][j] == 0:
                return
            A[i][j] = 0
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 0:
                    continue
                if i == 0 or j == 0 or i == len(A) - 1 or (j == len(A[i]) - 1):
                    dfs(i, j)
        res = sum([sum(row) for row in A])
        return res
