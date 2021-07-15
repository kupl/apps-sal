class Solution:
    def numSubseq(self, arr: List[int], target: int) -> int:
        
        arr=sorted(arr)
        l=0
        r=len(arr)-1
        
        mod=1000000007
        ans=0
        while(l<=r):
            if(arr[l]+arr[r] > target):
                r-=1    
            else:
                ans+=pow(2,r-l)
                l+=1
                
        return ans%mod
                

        
        
        

