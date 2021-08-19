from collections import deque


class Solution:

    def __init__(self):
        self.next_move = [(4, 6), (6, 8), (7, 9), (4, 8), (3, 0, 9), (), (1, 7, 0), (6, 2), (3, 1), (2, 4)]
        self.cache = {}

    def dfs(self, start, n):
        if n == 0:
            return 1
        if not self.cache.get((start, n)):
            total_numbers = 0
            for i in self.next_move[start]:
                total_numbers += self.dfs(i, n - 1)
            self.cache[start, n] = total_numbers
        return self.cache[start, n]

    def knightDialer(self, n: int) -> int:
        return sum([self.dfs(i, n - 1) for i in range(10)]) % (10 ** 9 + 7)
