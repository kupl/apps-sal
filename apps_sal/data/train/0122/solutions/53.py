class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints)
        maxRightSum = sum(cardPoints[size - k:])
        ans = maxRightSum
        currSum = maxRightSum
        for i in range(k):
            currSum = currSum - cardPoints[size - k + i] + cardPoints[i]
            ans = max(ans, currSum)
        return ans
