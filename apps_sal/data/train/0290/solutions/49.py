class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()

        def helper(cuts, memo, l, r):
            res = float('inf')
            key = (l, r)
            if key in memo.keys():
                return memo[key]
            for i in range(len(cuts)):
                if cuts[i] <= l or cuts[i] >= r:
                    continue
                cost = r - l
                res = min(helper(cuts, memo, l, cuts[i]) + cost + helper(cuts, memo, cuts[i], r), res)
            if res == float('inf'):
                res = 0
            memo[key] = res
            return res
        c = collections.defaultdict(int)
        return helper(cuts, c, 0, n)
