class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        largest = 0
        i = 0
        while(i<len(A)-1):
            largest = max(largest,A[i]+A[i+1]-1)
            if A[i]>A[i+1]:
                A[i],A[i+1]=A[i+1]+1,A[i]-1
            i += 1
        return largest
        
            

