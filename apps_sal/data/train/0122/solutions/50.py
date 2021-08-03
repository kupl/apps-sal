class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sums = [0] * (k + 1)
        right_sums = [0] * (k + 1)

        for i in range(k):
            left_sums[i + 1] = left_sums[i] + cardPoints[i]
            right_sums[i + 1] = right_sums[i] + cardPoints[len(cardPoints) - i - 1]

        res = 0
        for i in range(k + 1):  # we must include K as a choice
            j = k - i
            res = max(res, left_sums[i] + right_sums[j])

        return res
