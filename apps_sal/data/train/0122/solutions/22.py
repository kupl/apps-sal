class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        forwardSum = [m for m in cardPoints]
        backwardSum = cardPoints.copy()
        backwardSum.append(0)
        for c in range(1, len(cardPoints)):
            forwardSum[c] = forwardSum[c - 1] + forwardSum[c]

        for l in range(len(cardPoints) - 2, 0, -1):
            backwardSum[l] = backwardSum[l + 1] + backwardSum[l]
        maximum = 0
        for i in range(k - 1, -2, -1):
            if i != -1:
                maximum = max(maximum, forwardSum[i] + backwardSum[len(backwardSum) - 1 - (k - 1 - i)])
            else:
                maximum = max(maximum, backwardSum[len(backwardSum) - 1 - k])

        return maximum
