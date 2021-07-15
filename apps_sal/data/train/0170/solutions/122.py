class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        i = 0
        pref = 1
        while i<len(arr)-1:
            if arr[i]<=arr[i+1]:
                pref+=1
            else:
                break
            i+=1
        
        j = len(arr)-1
        suff = 1
        while j>0:
            if arr[j]>=arr[j-1]:
                suff+=1
            else:
                break
            j-=1
        
        ans = min(len(arr)-pref,len(arr)-suff)
        pref = i
        suff = j
        i = 0
        j = suff
        while i<=pref and j<len(arr):
            if arr[i]<=arr[j]:
                ans = min(ans,j-i-1)
                i+=1
            elif arr[j]<arr[i]:
                j+=1
        # ans = min(ans,j-i-1)
        return  max(0,ans)

