from collections import deque


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        first = deque(cardPoints[0:k])
        second = deque(cardPoints[len(cardPoints) - k:])
        final = 0

        firstSum = sum(first)
        secondSum = sum(second)

        for i in range(k):
            if firstSum > secondSum:
                final += first[0]
                firstSum -= first.popleft()
                secondSum -= second.popleft()

            else:
                final += second[len(second) - 1]
                firstSum -= first.pop()
                secondSum -= second.pop()

        return final
