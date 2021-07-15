class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        i = 0
        ans = float('-inf')
        
        for j in range(1,len(A)):
            ans = max(ans, A[i] + A[j] + i - j)
            
            if A[j] + j >= A[i] + i:
                i = j
        return ans
