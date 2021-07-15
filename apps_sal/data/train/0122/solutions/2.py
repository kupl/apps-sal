class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        result = curr = 0
        for i in range(-k, k):
            curr += cardPoints[i]
            if i >= 0:
                curr -= cardPoints[i - k]
            result = max(result, curr)
        return result
