class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n=len(arr)
        left,right=-1,-1
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                left=i+1
                break
        if left==-1:
            return 0
        for j in range(n-1, 0, -1):
            if arr[j]<arr[j-1]:
                right=j-1
                break
        if right==-1:
            return 0
        
        ans=min(right+1, n-left)
        i=0
        for j in range(right+1,n):
            while i<left and arr[i]<=arr[j]:
                i+=1
            ans=min(ans, j-i)
            if i==left:
                break
        return ans


