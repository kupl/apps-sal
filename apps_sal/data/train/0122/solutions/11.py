class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left, right = [0], [0]
        for i in range(len(cardPoints)):
            left.append(left[-1] + cardPoints[i])
            right.append(right[-1] + cardPoints[-i - 1])
        return max(left[i] + right[k - i] for i in range(k + 1))
