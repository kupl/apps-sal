class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        answer = 0
        left = [0] * len(cardPoints)
        right = [0] * len(cardPoints)
        for i in range(len(cardPoints)):
            if i == 0:
                left[0] = cardPoints[0]
            else:
                left[i] = left[i - 1] + cardPoints[i]
        for i in range(len(cardPoints) - 1, -1, -1):
            if i == len(cardPoints) - 1:
                right[-1] = cardPoints[-1]
            else:
                right[i] = right[i + 1] + cardPoints[i]
        for i in range(k + 1):
            if i == 0:
                Sum = right[-k]
            elif i == k:
                Sum = left[k - 1]
            else:
                Sum = left[k - i - 1] + right[-i]
            answer = max(answer, Sum)
        return answer
