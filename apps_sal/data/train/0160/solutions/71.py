from collections import defaultdict


def maxsum(piles, left, right, memo):
    if memo[left, right]:
        return memo[left, right]

    if left == right:
        return piles[left], 0

    y1, x1 = maxsum(piles, left + 1, right, memo)
    y2, x2 = maxsum(piles, left, right - 1, memo)

    if x1 + piles[left] < x2 + piles[right]:
        memo[left, right] = x2 + piles[right], y2
    else:
        memo[left, right] = x1 + piles[left], y1

    return memo[left, right]


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = defaultdict(int)

        x, y = maxsum(piles, 0, len(piles) - 1, memo)

        return True if x > y else False
