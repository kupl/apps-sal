class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        n = len(cardPoints)

        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + cardPoints[i]

        max_val = -1

        for i in range(k + 1):
            max_val = max(max_val, pre[i] + pre[n] - pre[n - k + i])

        return max_val
