class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # The Edge Case not needed here: if k > len(cardPoints) or k<=0: raise ValueErro('')
        # Your solution is O(N) and this solution is O(k)
        # Eventhough the real time is similar, O(k) is better
        left = [0] * (k+1)
        right = [0] * (k+1)
        for i in range(k):
            left[i+1] = left[i] + cardPoints[i]
            right[i+1] = right[i] + cardPoints[-i-1]
        return max(left[j]+right[k-j] for j in range(k+1))
