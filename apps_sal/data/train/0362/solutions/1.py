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
            nx = d.copy()
            for j in d:
                for k in r:
                    if not (j & (1 << k)):
                        nj = j | (1 << k)
                        nx[nj] = (nx.get(nj, 0) + d[j])
            d = nx
        return d.get((1 << n) - 1, 0) % MOD
