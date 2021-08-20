class Solution:

    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        mod = 10 ** 9 + 7
        DP = [[[0] * (P + 1) for _ in range(G + 1)] for _ in range(len(group) + 1)]
        DP[0][0][0] = 1
        for k in range(1, len(group) + 1):
            g = group[k - 1]
            p = profit[k - 1]
            for i in range(G + 1):
                for j in range(P + 1):
                    DP[k][i][j] = DP[k - 1][i][j]
                    if i - g < 0:
                        continue
                    DP[k][i][j] = DP[k - 1][i][j] + DP[k - 1][i - g][max(0, j - p)]
        ans = 0
        for i in range(G + 1):
            ans += DP[len(group)][i][P] % mod
        return ans % mod
        '\n        m = {}\n        mod = 10**9 + 7\n        def dfs(idx, g, p):\n            if idx == 0:\n                if (idx, g, p) == (0, 0, 0):\n                    return 1\n                return 0\n            #if g <= 0:\n            #    return 0\n            if (idx, g, p) in m:\n                return m[(idx, g, p)]\n            res = 0\n            res = (dfs(idx-1, g, p) + dfs(idx-1, g-group[idx-1], max(0, p-profit[idx-1])))%mod\n            m[(idx, g, p)] = res\n            return res\n        ans = 0\n        for i in range(G+1):\n            ans += dfs(len(group), i, P)%mod\n        return ans%mod\n        '
        '\n        m = {}\n        \n        def dfs(idx, g, p):\n            res = 0\n            if idx == 0:\n                if g >= group[0] and profit[0] >= p:\n                    res = 1\n                return res\n            if g <=0:\n                return 0\n            if p == 0:\n                \n            if (idx, g, p) in m:\n                return m[(idx, g, p)]\n            \n            res = m[(idx-1, g, p)] + dfs(idx-1, g-group[idx], max(0, p-profit[idx]))\n            m[(idx, g, p)] = res\n            return res\n        '
