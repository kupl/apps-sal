class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:  
        sub_len = len(cardPoints) - k
        localSum = 0
        localSum = sum(cardPoints[0: sub_len])
        localMin = localSum
        for i in range(sub_len, len(cardPoints)):
            localSum += cardPoints[i]
            localSum -= cardPoints[i - sub_len]
            localMin = min(localSum, localMin)
        return  sum(cardPoints) - localMin
