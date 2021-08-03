class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        dp = {}
        return self.recur(0, n, dp, cuts)

    def recur(self, l, r, dp, cuts):
        if (l, r) in dp:
            return dp[(l, r)]

        cost = r - l
        res = float('inf')
        for c in cuts:
            if c > l and c < r:
                res = min(res, self.recur(l, c, dp, cuts) + self.recur(c, r, dp, cuts) + cost)

        if res == float('inf'):
            dp[(l, r)] = 0
        else:
            dp[(l, r)] = res

        return dp[(l, r)]
