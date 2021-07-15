class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        self.memo = {}
        cuts = set(cuts)

        def dp(i, j):
            if (i, j) in self.memo:
                return self.memo[(i, j)]
            min_value = None
            for cut in cuts:
                if (cut > i) and (cut < j):
                    if min_value is None:
                        min_value = dp(i, cut) + dp(cut, j) + (j - i)
                    else:
                        min_value = min(min_value, dp(i, cut) + dp(cut, j) + (j-i))

            if min_value is None:
                min_value = 0
            self.memo[(i, j)] = min_value
            return min_value

        return dp(0, n)
