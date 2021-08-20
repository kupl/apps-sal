from collections import deque


class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        cards = n - k
        minimum = 0
        if cards != 0:
            sum1 = 0
            q = deque()
            for i in range(cards):
                q.append(cardPoints[i])
                sum1 += cardPoints[i]
            minimum = sum1
            for i in range(cards, n):
                first = q.popleft()
                q.append(cardPoints[i])
                sum1 -= first
                sum1 += cardPoints[i]
                if sum1 < minimum:
                    minimum = sum1
        print(minimum)
        return sum(cardPoints) - minimum
