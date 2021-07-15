class Solution:
    def numD(self,arr,n):
        count=0
        ans=0
        for i in range(len(arr)):
            count+=arr[i]
            if count>n:
                ans+=1
                count=arr[i]
        return ans+1
    
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l=-1
        r=25000000
        for i in range(len(weights)):
            if weights[i]>l:
                l=weights[i]
            #r+=weights[i]
        
        while l<=r:
            mid = (l+r)//2
            if self.numD(weights,mid)<=D:
                r=mid-1
            elif self.numD(weights,mid)>D:
                l=mid+1
            
        return l

