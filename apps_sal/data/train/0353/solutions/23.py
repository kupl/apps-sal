class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        left,right = 0,len(nums)-1
        count = 0
        
        dp = [0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            dp[i]=2*dp[i-1]+1
#        print (\"dp \",dp)
        while left<=right:
           
            while left<=right and nums[left] + nums[right]>target:
                right -=1
            count += dp[right-left+1]
#            print (\"-- \",left,\"  \",right, \"  count =\",count)
            while left<=right and nums[left] + nums[right]<=target:
                left +=1
            count -=dp[right-left+1]  
#            print (\"$$ \",left,\"  \",right, \"  count =\",count)
        
        return count %(10**9 +7)

    
    
    
    def totalS(self,N):
        if N<2: return N
        return 2* self.totalS(N-1) +1

