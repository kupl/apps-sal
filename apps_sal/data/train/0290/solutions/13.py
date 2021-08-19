class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:
        dp = {}
        position = {}
        cuts.sort()
        for i in range(len(cuts)):
            position[cuts[i]] = i

        def f(s, e):
            if (s, e) in dp:
                return dp[s, e]
            else:
                res = float('inf')
                i = 0
                if s < cuts[0]:
                    i = 0
                else:
                    i = position[s] + 1
                j = len(cuts) - 1
                if e > cuts[len(cuts) - 1]:
                    j = len(cuts) - 1
                else:
                    j = position[e] - 1
                if i > j:
                    dp[s, e] = 0
                    return 0
                for k in range(i, j + 1):
                    res = min(res, f(s, cuts[k]) + f(cuts[k], e) + e - s)
                dp[s, e] = res
                return dp[s, e]
        return f(0, n)
