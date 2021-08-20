class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)
        (pre, post) = ([0] * (n + 1), [0] * (n + 1))
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + cardPoints[i - 1]
        for i in range(1, n + 1):
            post[i] = post[i - 1] + cardPoints[n - i]
        best = 0
        for i in range(k + 1):
            best = max(best, pre[i] + post[k - i])
        return best
