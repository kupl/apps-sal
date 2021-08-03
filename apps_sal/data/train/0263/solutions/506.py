class Solution:
    def knightDialer(self, n: int) -> int:
        self.mod = 10**9 + 7
        total_path = 0
        self.d = {}
        for i in range(0, 4):
            for j in range(0, 3):
                total_path = (total_path + self.dfs(i, j, n)) % self.mod

        return total_path

    def dfs(self, i, j, n):
        if i < 0 or j < 0 or j >= 3 or i >= 4 or (i == 3 and j != 1):
            return 0

        if (i, j, n) in self.d:
            return self.d[(i, j, n)]

        if n == 1:
            return 1

        total = self.dfs(i - 1, j + 2, n - 1) % self.mod + self.dfs(i - 1, j - 2, n - 1) % self.mod + self.dfs(i + 1, j - 2, n - 1) % self.mod + self.dfs(i + 1, j + 2, n - 1) % self.mod + self.dfs(i + 2, j + 1, n - 1) % self.mod + self.dfs(i + 2, j - 1, n - 1) % self.mod + self.dfs(i - 2, j + 1, n - 1) % self.mod + self.dfs(i - 2, j - 1, n - 1) % self.mod

        self.d[(i, j, n)] = total
        return total
