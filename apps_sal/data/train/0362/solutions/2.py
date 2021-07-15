class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD = int(1e9) + 7
        n = len(hats)
        # dp = [[0 for _ in range(1 << n)] for _ in range(41)]
        d = {0: 1}
        rev = [[] for _ in range(41)]
        for i, h in enumerate(hats):
            for e in h:
                rev[e].append(i)
        for i in range(40):
            r = rev[i+1]
            nx = {}
            for j in d:
                nx[j] = (nx.get(j, 0) + d[j]) % MOD
                for k in r:
                    if not (j & (1 << k)):
                        nx[j | (1 << k)] = (nx.get(j | (1 << k), 0) + d[j]) % MOD
            d = nx
        return d.get((1 << n) - 1, 0)
