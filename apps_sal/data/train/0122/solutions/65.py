class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        size = len(cardPoints) - k
        min_sum = float('inf')
        left = 0
        right = 0
        window_sum = 0
        while right < len(cardPoints):
            window_sum += cardPoints[right]
            right += 1
            while right - left == size:
                min_sum = min(min_sum, window_sum)
                window_sum -= cardPoints[left]
                left += 1
        return sum(cardPoints) - min_sum
