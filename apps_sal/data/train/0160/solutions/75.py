class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        sums = [0] + list(itertools.accumulate(piles))
        def get_sum(i, j):
            return sums[j+1] - sums[i]
        
        n = len(piles)
        dp = [[-1]*n for _ in range(n)]
        def solve(i, j):
            if i > j:
                return 0
            if i == j:
                return piles[i]
            if dp[i][j] >= 0:
                return dp[i][j]
            sa = piles[i] + get_sum(i+1, j) - solve(i+1, j)
            sb = piles[j] + get_sum(i, j-1) - solve(i, j-1)
            dp[i][j] = max(sa, sb)
            return dp[i][j]
        alice = solve(0, len(piles)-1)
        return alice > get_sum(0, n-1) - alice

