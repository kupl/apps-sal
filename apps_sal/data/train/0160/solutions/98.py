class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = dict()
        return self.find(piles, 0, 0, True, 0, len(piles) - 1, memo)

    def find(self, piles, a_score, b_scord, is_a, front, end, memo):
        if front > end:
            return a_score > b_scord

        key = (front, end)
        if key in memo:
            return memo[key]

        if is_a:
            res = self.find(piles, a_score + piles[front], b_scord, not is_a, front + 1, end, memo) or self.find(piles, a_score + piles[end], b_scord, not is_a, front, end - 1, memo)
        else:
            res = self.find(piles, a_score, b_scord + piles[front], not is_a, front + 1, end, memo) or self.find(piles, a_score, b_scord + piles[end], not is_a, front, end - 1, memo)

        memo[key] = res
        return res
