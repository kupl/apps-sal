class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:

        def top_down(i, j, memo):
            if (i, j) not in memo:
                if j - i <= 1:
                    return 0
                memo[i, j] = float('inf')
                for c in cuts:
                    if c > i and c < j:
                        memo[i, j] = min(memo[i, j], j - i + top_down(i, c, memo) + top_down(c, j, memo))
            return memo[i, j] if memo[i, j] != float('inf') else 0
        return top_down(0, n, dict())
