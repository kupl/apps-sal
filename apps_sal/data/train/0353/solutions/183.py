class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums=sorted(nums)
        c=10**9+7
        left=0
        res=0
        right=len(nums)-1
        while(left<=right):
            if nums[left]+nums[right]<=target:
                res=(res+pow(2,(right-left)))%c
                left+=1
            else:
                right-=1
        return res        
                

