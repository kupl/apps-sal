class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        if not A:
            return 0
        temp=A[0]
        ans=-999
        for i in range(1, len(A)):
            ans=max(ans, temp+A[i]-i)
            temp=max(temp, A[i]+i)
        return ans
