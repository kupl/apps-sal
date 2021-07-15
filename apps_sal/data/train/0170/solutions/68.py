class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        peak=0
        while peak<len(arr)-1 and  arr[peak]<=arr[peak+1]:
            peak+=1
        if peak==len(arr)-1:
            return 0
        valley=len(arr)-1
        while valley>0 and  arr[valley]>=arr[valley-1]:
            valley=valley-1
        ans=min(valley,len(arr)-peak-1)
        i=0
        j=valley
        while i<=peak and j<len(arr):
            if arr[j]>=arr[i]:
                ans=min(ans,j-i-1)
                i+=1
            else:
                j+=1
        return ans
        
            
                
                

