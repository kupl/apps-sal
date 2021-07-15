class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        MOD = 10**9 + 7
        
        i, j , ans = 0, len(nums)-1, 0
        while i<=j:
            if nums[i]+nums[j]<=target:
                ans+=(2**(j-i))%MOD
                i+=1
            else:
                j-=1
        
        return ans%MOD
            
            

