class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        sumarr=sum(arr)
        maxsum=0
        currentsum=0
        for i in range(len(arr)):
            currentsum+=arr[i]
            if(currentsum<0):
                currentsum=0
            maxsum=max(maxsum,currentsum)
        if(sumarr>0):
            if(sumarr*k>maxsum):
                maxsum=sumarr*k
        maxprefixsum=0
        currentsum=0
        for i in range(len(arr)):
            currentsum+=arr[i]
            maxprefixsum=max(maxprefixsum,currentsum)
        maxsufixsum=0
        currentsum=0
        for i in range(len(arr)-1,-1,-1):
            currentsum+=arr[i]
            maxsufixsum=max(maxsufixsum,currentsum)
        if(k>=2):
            maxsum=max(maxsum,maxsufixsum+maxprefixsum)
        if(sumarr>0):
            maxsum=max(sumarr*(k-2)+maxsufixsum+maxprefixsum,maxsum)
        return maxsum%1000000007
            
            
        

