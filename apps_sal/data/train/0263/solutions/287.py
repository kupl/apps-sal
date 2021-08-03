class Solution:
    def knightDialer(self, n: int) -> int:
        # mod = int(1e9)+7
        # d = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7:[2,6], 8: [1,3], 9:[2, 4], 0: [4,6]}
        # cache = collections.defaultdict(int)
        # #@lru_cache(maxsize=None)
        # def dfs(i, n):
        #     #nonlocal d, cache
        #     if not n: return 1
        #     if (i, n) not in cache:
        #         s = sum(dfs(val, n-1) for val in d[i])
        #         cache[i, n] = s
        #         if i in [3,6,9]: cache[i-2, n] = s
        #         elif i in [1,4,7]: cache[i+2, n] = s
        #     return cache[i, n]
        #
        # return sum(dfs(i, n-1) for i in range(10)) % mod

        self.moves = [(4, 6), (6, 8), (7, 9), (4, 8), (3, 9, 0), (), (1, 7, 0), (2, 6), (1, 3), (2, 4)]
        return sum(self.knightDialer_(n, i) for i in range(10)) % (10**9 + 7)

    def knightDialer_(self, N, i, dp={}):
        if N == 1:
            return 1
        if (N, i) not in dp:
            dp[(N, i)] = sum(self.knightDialer_(N - 1, j) for j in self.moves[i])
        return dp[(N, i)]
