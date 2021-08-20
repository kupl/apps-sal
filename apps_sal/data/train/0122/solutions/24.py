class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        score = sum(cardPoints[:k])
        best = score
        for i in range(k):
            score += cardPoints[-(i + 1)] - cardPoints[k - i - 1]
            if score > best:
                best = score
        return best
