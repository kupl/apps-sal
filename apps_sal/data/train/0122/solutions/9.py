class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = [0] * (k + 1)
        right = [0] * (k + 1)
        for i in range(k):
            left[i + 1] = left[i] + cardPoints[i]
            right[i + 1] = right[i] + cardPoints[-i - 1]
        return max(left[j] + right[k - j] for j in range(k + 1))
