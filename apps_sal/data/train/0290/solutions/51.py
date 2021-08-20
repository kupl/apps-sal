class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:
        dp = {}

        def top_down(low, high, cuts):
            if (low, high) in dp:
                return dp[low, high]
            possible_cuts = [c for c in cuts if low < c < high]
            if not possible_cuts:
                return 0
            ans = float('inf')
            for mid in possible_cuts:
                ans = min(ans, top_down(low, mid, cuts) + top_down(mid, high, cuts))
            dp[low, high] = ans + high - low
            return dp[low, high]
        return top_down(0, n, cuts)
