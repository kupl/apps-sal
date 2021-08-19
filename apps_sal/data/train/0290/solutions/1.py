class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:

        @lru_cache(None)
        def cut(left, right):
            res = right - left
            min_subproblem = float('inf')
            for c in cuts:
                if left < c < right:
                    min_subproblem = min(min_subproblem, cut(left, c) + cut(c, right))
            if min_subproblem == float('inf'):
                return 0
            res += min_subproblem
            return res
        return cut(0, n)
