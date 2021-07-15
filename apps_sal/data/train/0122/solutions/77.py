class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        total = sum(cardPoints)
        
        nk = len(cardPoints) - k
        
        if nk == 0:
            return total
        
        current = sum(cardPoints[0:nk])
        max_score = current
        
        for i in range(1, k + 1):
            current = current - cardPoints[i - 1] + cardPoints[nk + i - 1]
            
            max_score = min(max_score, current)
            
        return total - max_score
