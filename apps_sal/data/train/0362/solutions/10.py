class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        h2p = defaultdict(list)
        for i, hat in enumerate(hats):
            for h in hat:
                h2p[h].append(i)
        n = len(hats)
 
        # bottom up
        dp, ndp = defaultdict(int), defaultdict(int)

        for hat in range(0, 41):
            for mask in range(1<<n):
                if mask == 0: ndp[mask] = 1
                else:
                    ndp[mask] = dp[mask]
                    for p in h2p[hat]:
                        if mask & (1<<p):
                            ndp[mask] += dp[mask ^ (1<<p)]
                            ndp[mask] %= 10**9+7
            dp, ndp = ndp, defaultdict(int)

        return dp[(1<<n)-1]
