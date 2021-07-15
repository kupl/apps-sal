class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
         
        def maxDelta(cuts, end):
            cuts.sort()
            cuts.append(end)
            cuts.append(0)

            md=0
            for i in range(len(cuts)-1):
                md=max(md,cuts[i]-cuts[i-1])
            
            return md
        
        def getGap(arr, n):
            prev=0
            i=0
            res=0
            while i<len(arr):
                res=max(arr[i]-prev, res)
                prev=arr[i]
                i+=1
            return max(n-prev, res)
    
        return (maxDelta(horizontalCuts, h)*maxDelta(verticalCuts, w))%(10**9 + 7)

        
        mh=maxDelta(horizontalCuts, h)
        mv=maxDelta(verticalCuts, w)
        
        return (mh*mv)%(10^9+7)
