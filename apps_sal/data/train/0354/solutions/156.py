class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = {(i, 1): 1 for i in range(6)}
        for i in range(n - 1):
            next_dp = collections.Counter()
            for (d, c), v in list(dp.items()):
                for cur in range(6):
                    if cur != d:
                        next_dp[(cur, 1)] += v
                    else:
                        if c + 1 <= rollMax[cur]:
                            next_dp[(cur, c + 1)] += v
            dp = next_dp

        return sum(dp.values()) % (10 ** 9 + 7)
#         def dfs(m, k, con):
#             if m == 1: return 1, 1
#             res = [0, 1]
#             for i in range(6):
#                 total, con = dfs(m - 1, i)
#                 if k == i:
#                     if con + 1 <= rollMax[i - 1]:
#                         res[0] += total
#                         res[1] = con + 1
#                 else:
#                     res += total

#         return sum(dfs(n, i) for i in range(6)) % (10 ** 9 + 7)
