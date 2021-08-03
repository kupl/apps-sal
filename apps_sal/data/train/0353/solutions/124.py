class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        left, right = 0, len(nums) - 1

        while left <= right:
            x0 = nums[left]
            if x0 + nums[right] > target:
                right -= 1
                continue

            count += 2**(right - left)
            left += 1

        return count % (10 ** 9 + 7)
