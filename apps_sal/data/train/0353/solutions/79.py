class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # time O(nlogn); space O(1)
        nums.sort()
        left, right = 0, len(nums) - 1
        res = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                res += pow(2, right-left)
                left += 1
            else:
                right -= 1
        
        return res % (10**9+7)

