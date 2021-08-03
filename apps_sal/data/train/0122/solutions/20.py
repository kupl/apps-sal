class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        #         cardLen = len(cardPoints)
        #         if cardLen == k:
        #             return sum(cardPoints)

        #         dp = {}
        #         def takeCard(l0, r0, k0):
        #             if k0 == 1:
        #                 return max(cardPoints[l0], cardPoints[r0])
        #             if (l0, r0, k0) in dp:
        #                 return dp[(l0, r0, k0)]

        #             ans = max(cardPoints[l0] + takeCard(l0+1, r0, k0-1), cardPoints[r0] + takeCard(l0, r0-1, k0-1))
        #             dp[(l0, r0, k0)] = ans

        #             return ans

        #         return takeCard(0, cardLen-1, k)
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
