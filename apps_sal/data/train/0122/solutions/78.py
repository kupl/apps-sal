class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        total = [0 for _ in range(len(cardPoints))]
        total[0] = cardPoints[0]

        for i in range(1, len(cardPoints)):
            total[i] = total[i - 1] + cardPoints[i]

        max_sum = 0
        for i in range(k + 1):
            left = total[k - i - 1] if k - i > 0 else 0
            right = total[-1] - total[len(cardPoints) - i - 1]
            if left + right > max_sum:
                max_sum = left + right

        return max_sum
