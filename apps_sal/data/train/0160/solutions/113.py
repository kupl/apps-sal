class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        memo = [[-1 for _ in range(len(piles))] for _ in range(len(piles))]
        return self.recursive(0, 0, len(piles) - 1, 0, 0, piles, memo)

    def recursive(self, turn, left_idx, right_idx, sum1, sum2, piles, memo):
        if left_idx >= right_idx:
            return sum1 > sum2
        if memo[left_idx][right_idx] != -1:
            return memo[left_idx][right_idx]
        if turn % 2 == 0:
            res = self.recursive(turn + 1, left_idx + 1, right_idx, sum1 + piles[left_idx], sum2, piles, memo) or self.recursive(turn + 1, left_idx, right_idx - 1, sum1 + piles[right_idx], sum2, piles, memo)
        else:
            res = self.recursive(turn + 1, left_idx + 1, right_idx, sum1, sum2 + piles[left_idx], piles, memo) or self.recursive(turn + 1, left_idx, right_idx - 1, sum1, sum2 + piles[right_idx], piles, memo)
        memo[left_idx][right_idx] = res
        return memo[left_idx][right_idx]
