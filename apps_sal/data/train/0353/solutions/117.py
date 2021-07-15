class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        idx, res = len(nums)-1, 0
        nums.sort()
        for i in range(len(nums)):
            while nums[i]+ nums[idx]> target and idx>=i:
                idx-=1
            if idx< i:
                break
            res += 2 ** (idx-i)
            
        return res%(10**9+7)
