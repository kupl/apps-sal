class Solution:

    def detect_cycle(self, grid, visited, rec_stack, i, j, M, N, prev):
        visited[i][j] = True
        rec_stack.append([i, j])
        for k, l in [[i, j - 1], [i - 1, j], [i, j + 1], [i + 1, j]]:
            if k >= 0 and l >= 0 and k < M and l < N and grid[i][j] == grid[k][l] and [k, l] != prev:
                if not visited[k][l]:
                    if self.detect_cycle(grid, visited, rec_stack, k, l, M, N, [i, j]) == True:
                        return True
                elif [k, l] in rec_stack:
                    return True
        rec_stack.pop()

    def containsCycle(self, grid: List[List[str]]) -> bool:
        M, N = len(grid), len(grid[0])
        visited = [[False] * N for _ in range(M)]
        rec_stack = []
        for i in range(M):
            for j in range(N):
                if not visited[i][j]:
                    if self.detect_cycle(grid, visited, rec_stack, i, j, M, N, [i, j]) == True:
                        return True
        return False
