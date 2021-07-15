class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        def getGap(arr, n):
            prev=0
            i=0
            res=0
            while i<len(arr):
                res=max(arr[i]-prev, res)
                prev=arr[i]
                i+=1
            return max(n-prev, res)
    
        return (getGap(horizontalCuts, h)*getGap(verticalCuts, w))%(10**9 + 7)
