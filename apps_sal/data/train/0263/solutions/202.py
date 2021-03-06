from collections import deque


class Solution:
    cache = {}
    d = [(4, 6), (6, 8), (7, 9), (4, 8), (3, 9, 0), (), (1, 7, 0), (2, 6), (1, 3), (2, 4)]

    def dfs(self, i, n):
        if n == 0:
            return 1
        elif (i, n) not in self.cache:
            self.cache[i, n] = sum((self.dfs(val, n - 1) for val in self.d[i]))
            if i in [1, 4, 7]:
                self.cache[i + 2, n] = self.cache[i, n]
            elif i in [3, 6, 9]:
                self.cache[i - 2, n] = self.cache[i, n]
        return self.cache[i, n]

    def knightDialer(self, n: int) -> int:
        return sum((self.dfs(i, n - 1) for i in range(10))) % (int(1000000000.0) + 7)
