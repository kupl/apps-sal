class Solution:

    def dfs(self, i, N):
        if N == 1:
            return 1
        if (i, N) in self.memo:
            return self.memo[i, N]
        ans = 0
        for nxt in self.map[i]:
            ans += self.dfs(nxt, N - 1)
        self.memo[i, N] = ans
        return ans

    def knightDialer(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 10
        self.map = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        self.memo = {}
        ans = 0
        for i in range(10):
            if i == 5:
                continue
            ans = (ans + self.dfs(i, n)) % (10 ** 9 + 7)
        return ans
