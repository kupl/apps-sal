class Solution:

    def numberWays(self, hats: List[List[int]]) -> int:
        hat_per_map = defaultdict(list)
        for (idx, i) in enumerate(hats):
            for j in i:
                hat_per_map[j - 1].append(idx)

        @lru_cache(None)
        def dp(hat, mask):
            if mask == (1 << len(hats)) - 1:
                return 1
            if hat >= 40:
                return 0
            ans = dp(hat + 1, mask) % 1000000007
            for i in hat_per_map[hat]:
                if not mask & 1 << i:
                    ans += dp(hat + 1, mask | 1 << i) % 1000000007
            return ans
        return dp(0, 0) % 1000000007
