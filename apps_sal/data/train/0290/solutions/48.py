class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = sorted(cuts)
        memo = {}
        t_cuts = [0] + cuts + [n]
        N = len(t_cuts)
        for i in range(1, N):
            memo[t_cuts[i - 1], t_cuts[i]] = 0

        def dp(s, e):
            if (s, e) in memo:
                return memo[s, e]
            filtered_cuts = [cut for cut in cuts if cut > s and cut < e]
            if len(filtered_cuts) == 0:
                return 0
            ans = math.inf
            for cut in filtered_cuts:
                ans = min(ans, e - s + dp(s, cut) + dp(cut, e))
            memo[s, e] = ans
            return memo[s, e]
        ans = dp(0, n)
        return ans
