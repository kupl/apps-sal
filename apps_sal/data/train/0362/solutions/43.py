class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        tot = len(hats)
        h = [[False] * tot for i in range(41)]
        for i in range(len(hats)):
            for j in range(len(hats[i])):
                h[hats[i][j]][i] = True

        f = [[0] * (1 << tot) for i in range(41)]
        f[0][0] = 1
        mod = 10**9 + 7
        for i in range(41):
            for j in range(1 << tot):
                f[i][j] = (f[i][j] + f[i - 1][j]) % mod
                for k in range(tot):
                    if (j & (1 << k)) != 0 and h[i][k]:
                        f[i][j] = (f[i][j] + f[i - 1][j ^ (1 << k)]) % mod
        return f[40][(1 << tot) - 1]
