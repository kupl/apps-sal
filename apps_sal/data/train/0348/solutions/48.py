class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        if len(arr)==1:
            return arr[0]
        
        def helper(arr):
            n=len(arr)
            dp=[0]*n

            if arr==[]:
                return 0
            else:
                res=0
                curr=arr[0]
                dp[0]=arr[0]
                for i in range(1,len(arr)):

                    
                    curr=max(curr+arr[i],arr[i])
                   
                    
                    res=max(res,curr)
                    dp[i]=curr
                    # print(res)
                return dp,res
            
        lp,best=helper(arr)
        rp,best=helper(arr[::-1])
        rp=rp[::-1]
            
        print(lp,rp)

        ans=-1
        for k in range(0,len(arr)):
            
            val=rp[k+1] if k<len(arr)-1 else 0 
            val2=lp[k-1]  if k>0 else 0
            print(val2,val)
            ans=max(ans,best,val+val2,val,val2)
        if ans==0:
            return -1
        return ans
