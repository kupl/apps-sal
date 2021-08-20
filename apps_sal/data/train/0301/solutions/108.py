class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        (m, n) = (len(A), len(B))
        grid = [[0 for i in range(n)] for i in range(m)]
        for j in range(m):
            for i in range(n):
                av = A[j]
                bv = B[i]
                topleft = 0
                top = 0
                left = 0
                if 0 <= j - 1 < m and 0 <= i - 1 < n:
                    topleft = grid[j - 1][i - 1]
                if 0 <= j - 1 < m:
                    top = grid[j - 1][i]
                if 0 <= i - 1 < n:
                    left = grid[j][i - 1]
                if av == bv:
                    grid[j][i] = topleft + 1
                else:
                    grid[j][i] = max(top, left)
        return grid[-1][-1]
