class Solution:
    def knightDialer(self, n: int) -> int:
        adj = {1: [6, 8], 2: [7, 9], 3: [8, 4], 4: [0, 9, 3], 5: [], 6: [7, 1, 0], 7: [6, 2], 8: [3, 1], 9: [4, 2], 0: [6, 4]}
        res = 0
        memo = collections.defaultdict(int)
        for i in range(10):
            res = (res + self.top_down(memo, adj, n - 1, i)) % (10**9 + 7)
        return res

    def top_down(self, memo, adj, n, cur):
        if n == 0:
            return 1
        if (cur, n) not in memo:
            for nb in adj[cur]:
                memo[(cur, n)] += self.top_down(memo, adj, n - 1, nb) % (10**9 + 7)
        return memo[(cur, n)]

#         jump = {1:[6,8], 2:[7,9], 3:[8,4], 4:[0,9,3], 5:[], 6:[7,1,0], 7:[6,2], 8:[3,1], 9:[4,2], 0:[6,4]}
#         # dp = [1]*10
#         # for _ in range(n-1):
#         #     nxt = [0]*10
#         #     for i in range(10):
#         #         for j in jump[i]:
#         #             nxt[j] += dp[i]
#         #     dp = nxt
#         # return sum(dp)%(10**9+7)

#     def count_paths(self, start, n, adj):
#         if not n: return 1
#         dp = {v:1 for v in adj.keys()}
#         return self.helper([start], n, adj)

#     def helper(self, cur, n, adj):
#         if not n:
#             return len(cur)
#         nxt = []
#         for u in cur:
#             nxt.extend(adj[u])
#         return self.helper(nxt, n-1, adj)
