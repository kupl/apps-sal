class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints) - k
        current = 0
        for i in range(n):
            current += cardPoints[i]
        result = current

        for i in range(1, k + 1):
            current -= cardPoints[i - 1]
            current += cardPoints[i + n - 1]
            result = min(result, current)

        return sum(cardPoints) - result
