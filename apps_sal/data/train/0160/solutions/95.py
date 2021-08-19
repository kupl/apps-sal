class Solution:

    def stoneGame(self, piles):

        def dp(piles, l, r, memo):
            if l > r:
                return 0
            if (l, r) in memo:
                return memo[l, r]
            op1 = piles[l] - dp(piles, l + 1, r, memo)
            op2 = piles[r] - dp(piles, l, r - 1, memo)
            stone = max(op1, op2)
            memo[l, r] = stone
            return stone
        return dp(piles, 0, len(piles) - 1, {}) > 0
