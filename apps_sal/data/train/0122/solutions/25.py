class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftsum = [0] * len(cardPoints)
        rightsum = [0] * len(cardPoints)
        n = len(cardPoints)
        leftsum[0] = cardPoints[0]
        rightsum[n - 1] = cardPoints[n - 1]
        for i in range(1, n):
            leftsum[i] = leftsum[i - 1] + cardPoints[i]
            rightsum[n - 1 - i] = rightsum[n - 1 - i + 1] + cardPoints[n - 1 - i]

        res = max(leftsum[k - 1], rightsum[-(k - 1 + 1)])

        for i in range(k - 1):

            res = max((leftsum[i] + rightsum[-(k - i - 1)]), res)

        return res
