class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:

        n = len(hats)
        fullMask = (1 << n) - 1
        mp = defaultdict(list)

        for idx, i in enumerate(hats):
            for hat in i:
                mp[hat - 1].append(idx)

        mod = 10**9 + 7

        @lru_cache(None)
        def dp(hat, mask):
            if mask == fullMask:
                return 1
            if hat >= 40:
                return 0

            ans = dp(hat + 1, mask) % mod
            for person in mp[hat]:
                if not mask & (1 << person):
                    ans += dp(hat + 1, mask ^ (1 << person))
                    ans %= mod
            return ans % mod

        return dp(0, 0) % mod
