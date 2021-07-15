class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        sum1=sum(arr)
        low=0
        min1=[float('Inf')]
        ans=[0]
        def check(mid,target):
            sum1=0
            for i in arr:
                if i>mid:
                    sum1+=mid
                else:
                    sum1+=i
            
               
            return sum1
        
        def binary(low,high,target):
            mid=(low+high)//2
           
            if low>high:
                return 
            x=check(mid,target)
            
            if x<target:
                
                if abs(target-x)<min1[0]:
                    ans[0]=mid
                   
                    min1[0]=abs(target-x)
                if abs(target-x)==min1[0]:
                    ans[0]=min(mid,ans[0])
                binary(mid+1,high,target)
            else:
                if abs(target-x)<min1[0]:
                    ans[0]=mid
                    min1[0]=abs(target-x)
                elif abs(target-x)==min1[0]:
                    ans[0]=min(mid,ans[0])
                
                binary(low,mid-1,target)
        binary(low,max(arr),target)
        return ans[0]
