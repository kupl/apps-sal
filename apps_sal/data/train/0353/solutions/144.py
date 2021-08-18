class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        count = 0

        nums.sort()

        for i in range(len(nums)):

            if (nums[i] * 2) > target:

                break

            left = i

            right = len(nums) - 1

            while left < right:

                mid = (left + right + 1) // 2

                if nums[i] + nums[mid] <= target:

                    left = mid

                else:

                    right = mid - 1

            count += (2 ** (left - i))

        return count % (10 ** 9 + 7)
