class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        @lru_cache(None)
        def cut(left, right):
            # if not subcuts:
            #     return 0
            # elif (left, right) in dp:
            #     return dp[(left, right)]

            res = right - left
            min_subproblem = float('inf')
            for c in cuts:
                if left < c < right:
                    min_subproblem = min(min_subproblem, cut(left, c) + cut(c, right))

            if min_subproblem == float('inf'):
                return 0

            res += min_subproblem
            # dp[(left, right)] = res
            return res

        # dp = {}

        return cut(0, n)
