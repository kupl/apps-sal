class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        # [1,2,3,-1,-2,3,0,-3,-4,1,2]
        # [*,*,*,*,*,*,-,*,*,*,*]
        # [-1,1,1,2,3]
        # [-,*,*,*,*]
        
        cp=1
        fp=-1
        fn=None
        ans=0
        
        for i,n in enumerate(nums):
            cp=n*cp
            if cp<0:
                
                if fn is None:
                    fn=ln=i
                else:
                    ln=i
                ans=max(ln-fn,ans)
            elif cp>0:
                lp=i
            
                ans=max(lp-fp,ans)
            
            if n==0:
                cp=1
                fp=i
                fn=None
        
        return ans
                
                

