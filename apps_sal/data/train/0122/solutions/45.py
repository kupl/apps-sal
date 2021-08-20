class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints) - k
        (l, r, res, count) = (0, 0, sum(cardPoints[:n]), 0)
        while r < len(cardPoints):
            count += cardPoints[r]
            if r >= n:
                count -= cardPoints[l]
                l += 1
                res = min(res, count)
            r += 1
        return sum(cardPoints) - res
