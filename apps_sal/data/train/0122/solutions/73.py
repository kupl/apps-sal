class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        score = 0
        l = k
        prefix = [0]
        for i in range(len(cardPoints)):
            prefix.append(prefix[-1] + cardPoints[i])
        for i in range(k + 1):
            score = max(score, prefix[l] + prefix[-1] - prefix[-1 - i])
            l -= 1
        return score
