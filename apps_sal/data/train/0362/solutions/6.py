class Solution:

    def numberWays(self, hats: List[List[int]]) -> int:
        h2p = defaultdict(list)
        n = len(hats)
        mod = 10 ** 9 + 7
        for (p, hat_list) in enumerate(hats):
            for h in hat_list:
                h2p[h].append(p)
        '\n        def dp(h, mask):\n            if (h, mask) in memo:\n                return memo[(h,mask)]\n            \n            if mask == (1 << n) - 1:\n                return 1\n        \n            if h > 40:\n                return 0\n            \n            ans = dp(h+1, mask)\n            \n            if h in h2p:\n                peoples = h2p[h]\n                \n                for p in peoples:\n                    if mask & (1 << p) == 0:\n                        mask |= (1 << p)\n                        ans += dp(h+1, mask)\n                        mask ^= (1 << p)\n            \n            memo[(h,mask)] = ans\n            \n            return ans\n        \n        memo = {}\n        \n        return dp(0, 0) % mod\n        '
        m = 1 << n
        dp = [[0] * m for _ in range(41)]
        dp[0][0] = 1
        for h in range(1, 41):
            for mask in range(m):
                dp[h][mask] = dp[h - 1][mask]
                for p in h2p[h]:
                    if mask & 1 << p != 0:
                        dp[h][mask] += dp[h - 1][mask ^ 1 << p]
        return dp[40][m - 1] % mod
