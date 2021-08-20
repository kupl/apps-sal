class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        curr_max = sum(cardPoints[0:k])
        curr_sum = curr_max
        for i in range(1, k + 1):
            curr_sum = curr_sum - cardPoints[k - i] + cardPoints[-i]
            curr_max = max(curr_max, curr_sum)
        return curr_max
