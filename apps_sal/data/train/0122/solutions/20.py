class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cardLen = len(cardPoints)
        frontSum = [0]
        for num in cardPoints:
            frontSum.append(frontSum[-1] + num)
        backSum = [0 for _ in range(cardLen + 1)]
        for i in range(cardLen - 1, -1, -1):
            backSum[i] = cardPoints[i] + backSum[i + 1]
        ans = frontSum[k]
        for i in range(k):
            ans = max(ans, frontSum[i] + backSum[-(k - i) - 1])
        return ans
