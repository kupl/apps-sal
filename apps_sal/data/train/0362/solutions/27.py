class Solution:

    def numberWays(self, hats: List[List[int]]) -> int:
        dp = {}
        n_ppl = len(hats)
        hat_2_ppl = {}
        for i in range(n_ppl):
            for hat in hats[i]:
                hat_2_ppl[hat] = hat_2_ppl.get(hat, []) + [i]

        def dfs(hat, mask):
            if mask == (1 << n_ppl) - 1:
                return 1
            if hat > 40:
                return 0
            if hat in dp and mask in dp[hat]:
                return dp[hat][mask]
            res = dfs(hat + 1, mask)
            for ppl in hat_2_ppl.get(hat, []):
                if not mask & 1 << ppl:
                    res += dfs(hat + 1, mask | 1 << ppl)
                    res %= 1000000000 + 7
            dp[hat] = dp.get(hat, {})
            dp[hat][mask] = res
            return res
        return dfs(1, 0)
