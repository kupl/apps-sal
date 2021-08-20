class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if not cardPoints or k == 0:
            return 0
        for i in range(1, len(cardPoints)):
            cardPoints[i] += cardPoints[i - 1]
        if k == len(cardPoints):
            return cardPoints[-1]
        ans = cardPoints[k - 1]
        for i in range(1, k + 1):
            print(i)
            ans = max(ans, cardPoints[k - i] + cardPoints[-1] - cardPoints[-i])
            print(cardPoints[k - i], cardPoints[-1] - cardPoints[-i])
        return max(ans, cardPoints[-1] - cardPoints[-(k + 1)])
