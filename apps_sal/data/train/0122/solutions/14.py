class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        (left, right) = ([0], [0])
        for i in range(k):
            left.append(left[-1] + cardPoints[i])
            right.append(right[-1] + cardPoints[len(cardPoints) - 1 - i])
        res = 0
        for i in range(k + 1):
            x = left[i] + right[k - i]
            res = max(res, x)
        return res
