class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        return self.cut(0, n, set(cuts), {})

    def cut(self, i, j, cuts, dp):
        v = float('inf')
        if (i, j) in dp:
            return dp[(i, j)]
        for x in cuts:
            if i < x and j > x:
                v = min(v, j - i + self.cut(i, x, cuts, dp) + self.cut(x, j, cuts, dp))
        dp[(i, j)] = v if v != float('inf') else 0
        return dp[(i, j)]
