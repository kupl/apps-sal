class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) == 1:
            return 1
        dp_grid = [[0] * 2 for i in range(len(A))]
        for i in range(len(A))[::-1]:
            if i == len(A) - 1:
                dp_grid[i] = [1, 1]
            elif A[i + 1] > A[i]:
                dp_grid[i][0] = 1 + dp_grid[i + 1][1]
                dp_grid[i][1] = 1
            elif A[i + 1] < A[i]:
                dp_grid[i][1] = 1 + dp_grid[i + 1][0]
                dp_grid[i][0] = 1
            else:
                dp_grid[i] = [1, 1]
        return max([max(i) for i in dp_grid])
