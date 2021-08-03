class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        remainCnt = len(cardPoints) - k
        if remainCnt == 0:
            return sum(cardPoints)
        minRemainSum = float('inf')
        curr = 0
        cnt = 0
        for i in range(len(cardPoints)):
            cnt += 1
            curr += cardPoints[i]
            if cnt == remainCnt:
                minRemainSum = min(minRemainSum, curr)
                curr -= cardPoints[i + 1 - cnt]
                cnt -= 1

        return sum(cardPoints) - minRemainSum
