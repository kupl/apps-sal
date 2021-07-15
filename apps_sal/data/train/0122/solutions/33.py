class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Sliding window of length k
        ans = total = sum(cardPoints[:k])
        for i in range(1, k+1):
            total -= cardPoints[k-i]
            total += cardPoints[-1-i+1]
            ans = max(ans, total)
        return ans

