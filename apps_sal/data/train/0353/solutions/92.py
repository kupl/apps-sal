class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        md=10**9 + 7
        left=0
        res=0
        right=len(nums)-1
        while(left<=right):
            if nums[left]+nums[right]<=target:
                res=(res+pow(2,right-left,md))%md
                left=left+1
            else:
                right=right-1
        return res
