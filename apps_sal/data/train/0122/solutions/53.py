class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints)
        maxRightSum = sum(cardPoints[size - k:])
        ans = maxRightSum
        currSum = maxRightSum
        # sum with left
        for i in range(k):
            currSum = currSum - cardPoints[size - k + i] + cardPoints[i]
            ans = max(ans, currSum)
        return ans
    # def maxScore(self, cardPoints: List[int], k: int) -> int:
    #     windowEnd = 0
    #     size = len(cardPoints) - k
    #     ans = float(\"inf\")
    #     currSum = 0
    #     for windowStart, point in enumerate(cardPoints):
    #         currSum += point
    #         if windowStart - windowEnd + 1 > size:
    #             currSum -= cardPoints[windowEnd]
    #             windowEnd += 1
    #         if windowStart - windowEnd + 1 == size:
    #             ans = min(ans, currSum)
    #     return sum(cardPoints) - ans
