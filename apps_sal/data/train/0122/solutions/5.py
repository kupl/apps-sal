class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints) - k
        minSum = float('inf')
        cur = 0
        left = 0
        for (i, v) in enumerate(cardPoints):
            cur += v
            if i - left + 1 > size:
                cur -= cardPoints[left]
                left += 1
            if i - left + 1 == size:
                minSum = min(minSum, cur)
        return sum(cardPoints) - minSum
