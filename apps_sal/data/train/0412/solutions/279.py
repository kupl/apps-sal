class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
           if target<d or target>d*f:
                return 0
           if target==d*f:
              return 1
           mem={};mod=int(1e9+7)
           def dice(k,target):
                if target==0:
                    return 0
                if k==1:
                    if target<=f:
                       return 1
                    else:
                        return 0
                if (k,target) in mem:
                    return mem[(k,target)]
                ans=0 
                for i in range(1,f+1):
                    if target>=i and target<=f*k:
                        ans+=dice(k-1,target-i)%mod
                ans%=mod
                mem[(k,target)]=ans
                return ans
           return dice(d,target) 
