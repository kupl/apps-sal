class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        psum = sum(cardPoints[:k])
        res = psum
        n = len(cardPoints)
        for i in range(k):
            psum += cardPoints[n - i - 1] - cardPoints[k - i - 1]
            res = max(res, psum)
        return res
