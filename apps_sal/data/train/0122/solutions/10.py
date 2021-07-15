class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:        
        left_cumsum = [0]
        right_cumsum = [0]
        for p in cardPoints[:k+1]:
            left_cumsum.append(left_cumsum[-1] + p)
        for p in reversed(cardPoints[-(k+1):]):
            right_cumsum.append(right_cumsum[-1] + p)
        
        result = 0
        for i in range(k+1):
            result = max(result, left_cumsum[i] + right_cumsum[k-i])
        return result
