class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        j = len(cardPoints) - 1
        ms = 0

        for i in range(k):
            ms += cardPoints[j]
            j -= 1

        cand = ms

        for i in range(k):
            cand += cardPoints[i] - cardPoints[j + 1]
            j += 1
            ms = max(cand, ms)

        return ms
