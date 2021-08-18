from collections import defaultdict


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        self.dp_table = defaultdict(int)

        def maximize_score_gap(piles, left, right):

            if left == right:
                return piles[left]

            if (left, right) in self.dp_table:
                return self.dp_table[(left, right)]

            choose_left = piles[left] - maximize_score_gap(piles, left + 1, right)
            choose_right = piles[right] - maximize_score_gap(piles, left, right - 1)

            self.dp_table[(left, right)] = max(choose_left, choose_right)

            return self.dp_table[(left, right)]

        score_gap_for_alex = maximize_score_gap(piles, left=0, right=len(piles) - 1)

        return score_gap_for_alex > 0
