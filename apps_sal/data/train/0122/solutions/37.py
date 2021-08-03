class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        n = len(cardPoints)

        cum_sum = [0 for i in range(n)]
        cum_sum[0] = cardPoints[0]
        rev_sum = [0 for i in range(n)]
        rev_sum[0] = cardPoints[-1]

        for i in range(1, n):
            cum_sum[i] = cum_sum[i - 1] + cardPoints[i]
            rev_sum[i] = rev_sum[i - 1] + cardPoints[n - i - 1]

        max_sum = max(cum_sum[k - 1], rev_sum[k - 1])

        for i in range(1, k):
            max_sum = max(max_sum, (cum_sum[i - 1] + rev_sum[k - i - 1]))

        return max_sum
