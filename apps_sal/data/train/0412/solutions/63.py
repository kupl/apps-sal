class Solution:
    def helper(self,d,f,target,cursum,dp):
        if(d==0):
            if(target==cursum):
                return 1
            else:
                return 0
        if(cursum>target):
            return 0
        cnt = 0
        if((d,cursum) in dp):
            return dp[(d,cursum)]
        for i in range(1,f+1):
            cnt+=self.helper(d-1,f,target,cursum+i,dp)
        dp[(d,cursum)]=cnt%(pow(10,9)+7)
        return cnt%(pow(10,9)+7)
    
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp={}
        return self.helper(d,f,target,0,dp)
