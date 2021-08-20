class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        curr_max = sum(cardPoints[:k])
        ans = curr_max
        for i in range(1, k + 1):
            curr_max += cardPoints[-i] - cardPoints[k - i]
            ans = max(ans, curr_max)
        return ans
