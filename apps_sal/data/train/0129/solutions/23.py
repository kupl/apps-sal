class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ans = 0
        best_pre = 0
        for i in range(1,len(A)):
            ans = max(ans, A[best_pre]+best_pre + A[i]- i)
            if A[i]+i >  A[best_pre] + best_pre:
                best_pre = i
        return ans

