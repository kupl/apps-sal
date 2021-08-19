class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) < k:
            return 0
        if len(cardPoints) == k:
            return sum(cardPoints)
        n = len(cardPoints)
        (res, cur) = (sum(cardPoints[:k]), sum(cardPoints[:k]))
        for i in range(k):
            cur += cardPoints[n - i - 1] - cardPoints[k - 1 - i]
            res = max(res, cur)
        return res
