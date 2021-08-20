class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        dp = [[-1 for x in range(len(piles))] for y in range(len(piles))]

        def recur_dp(si, ei, turn):
            if si > ei:
                return 0
            if dp[si][ei] != -1:
                return dp[si][ei]
            if turn == 0:
                start = recur_dp(si + 1, ei, 1 - turn) + piles[si]
                end = recur_dp(si, ei - 1, 1 - turn) + piles[ei]
                dp[si][ei] = max(start, end)
                return dp[si][ei]
            else:
                start = recur_dp(si + 1, ei, 1 - turn) - piles[si]
                end = recur_dp(si, ei - 1, 1 - turn) - piles[ei]
                dp[si][ei] = min(start, end)
                return dp[si][ei]
        recur_dp(0, len(piles) - 1, 0)
        return dp[0][len(piles) - 1] >= 0
