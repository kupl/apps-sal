class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints) - k
        min = 0
        window = 0
        all = 0
        for i in range(n):
            window += cardPoints[i]
        min = window
        all = window
        for x in range(k):
            all += cardPoints[x + n]
            window -= cardPoints[x]
            window += cardPoints[x + n]
            if window < min:
                min = window
        return all - min
