class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10**9 + 7
        left = 0
        right = len(nums) - 1
        res = 0 
        while(left <= right):
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                num_inside = right - left
                res = (res + pow(2, num_inside, mod)) % mod
                left += 1
        return res

