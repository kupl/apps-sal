class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        htop = [[] for i in range(41)]  # htop: hat to people list
        for p, prefer_hats in enumerate(hats):
            for h in prefer_hats:
                htop[h].append(p)
        htop = list([h for h in htop if h])  # filter out hats no one wants

        num_hats, num_people = len(htop), len(hats)
        if num_hats < num_people:
            return 0

        MOD = 10**9 + 7

        @functools.lru_cache(None)
        def dp(i, mask):
            if bin(mask).count('1') == num_people:
                return 1
            if i == num_hats:
                return 0
            res = dp(i + 1, mask)  # not using the current hat
            for p in htop[i]:
                if mask & (1 << p) == 0:
                    mask |= 1 << p
                    res += dp(i + 1, mask)
                    mask ^= 1 << p
            return res % MOD
        return dp(0, 0)
# class Solution:
#     def numberWays(self, hats: List[List[int]]) -> int:
#         hat2ppl = defaultdict(set)
#         for i, hats_i in enumerate(hats):
#             for h in hats_i:
#                 hat2ppl[h].add(i)
#         if len(hats) > len(hat2ppl): return 0
#         @lru_cache(None)
#         def dfs(h, mask):
#             print(h, mask)
#             if h == 40: return
#             if mask == (1 << len(hats)) - 1: return 1
#             dfs(h+1, mask)
#             ans = 0
#             for p in hat2ppl.get(h, set()):
#                 x = 1 << p
#                 if mask & x == 0:
#                     mask |= x
#                     ans += dfs(h+1, mask)
#                     mask ^= x
#             return ans % (10**9 + 7)
#         return dfs(0, 0)
