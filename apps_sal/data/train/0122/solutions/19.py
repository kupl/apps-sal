class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        runningsum = 0
        start = end = 0
        total = sum(cardPoints)
        minsum = float('inf')
        while end < len(cardPoints):
            runningsum += cardPoints[end]
            if end - start + 1 > n - k:
                runningsum -= cardPoints[start]
                start += 1
            if end - start + 1 == n - k:
                minsum = min(minsum, runningsum)
            end += 1
        return total - minsum
