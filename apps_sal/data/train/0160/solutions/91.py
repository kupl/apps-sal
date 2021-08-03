class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        if not piles:
            return False
        n = len(piles)
        return self.helper(0, n - 1, piles, 0, 0, 1, {})

    def helper(self, left, right, piles, scoreA, scoreB, isPlayerA, memo):
        if left > right:
            return scoreA > scoreB

        if (left, right, isPlayerA) in memo:
            return memo[(left, right, isPlayerA)]

        if isPlayerA:
            res = self.helper(left + 1, right, piles, scoreA + piles[left], scoreB, 1 - isPlayerA, memo) or self.helper(left, right - 1, piles, scoreA + piles[right], scoreB, 1 - isPlayerA, memo)
        else:
            res = self.helper(left + 1, right, piles, scoreA, scoreB + piles[left], 1 - isPlayerA, memo) or self.helper(left, right - 1, piles, scoreA, scoreB + piles[right], 1 - isPlayerA, memo)

        memo[(left, right, isPlayerA)] = res
        return res
