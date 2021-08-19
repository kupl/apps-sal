class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        sums = [0] * (n + 1)
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + cardPoints[i - 1]
        ans = float('inf')
        for i in range(k + 1):
            ans = min(ans, sums[i + n - k] - sums[i])
        return sums[-1] - ans
