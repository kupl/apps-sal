class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:

        def dp(s, e):
            if (s, e) in memo:
                return memo[s, e]
            ans = 2 ** 31
            canCut = False
            for cut in cuts:
                if s < cut < e:
                    canCut = True
                    a1 = dp(s, cut) + dp(cut, e) + e - s
                    ans = min(ans, a1)
            if not canCut:
                return 0
            memo[s, e] = ans
            return ans
        memo = {}
        return dp(0, n)
