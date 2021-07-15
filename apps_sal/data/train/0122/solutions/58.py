class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        left = n - k
        mini = sum(cardPoints[:left])
        cur = mini
        for i in range(left, n):
            cur = cur - cardPoints[i-left] + cardPoints[i]
            mini = min(mini, cur)
        
        return sum(cardPoints) - mini
