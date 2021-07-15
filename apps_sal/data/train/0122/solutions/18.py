class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s = sum(cardPoints)
        if k >= len(cardPoints):
            return s
        maxPoint = 0
        cur = 0
        j = 0
        # i-j+k == n
        n = len(cardPoints)
        for i, point in enumerate(cardPoints):
            if i-j+k > n-1:
                cur -= cardPoints[j]
                j += 1
            cur += point
            if i-j+k == n-1:
                maxPoint = max(maxPoint, s-cur)
        return maxPoint

