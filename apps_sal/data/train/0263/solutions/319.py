class Solution:

    def __init__(self):
        self.pos_2_pos_map = {1: (6, 8), 2: (7, 9), 3: (4, 8), 4: (3, 0, 9), 5: tuple(), 6: (7, 1, 0), 7: (2, 6), 8: (1, 3), 9: (4, 2), 0: (4, 6)}

    def dfs(self, position, n, memo):
        if n == 0:
            return 1
        if (position, n) in memo:
            return memo[position, n]
        counts = 0
        for nei in self.pos_2_pos_map[position]:
            counts += self.dfs(nei, n - 1, memo)
        memo[position, n] = counts
        return counts

    def knightDialer(self, n: int) -> int:
        memo = {}
        counts = 0
        for position in self.pos_2_pos_map:
            counts += self.dfs(position, n - 1, memo)
        return counts % (10 ** 9 + 7)
