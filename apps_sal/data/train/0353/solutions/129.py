class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)

        left = 0
        right = len(nums) - 1

        result = 0

        while True:

            while left <= right and (nums[left] + nums[right] > target):
                right -= 1

            if right < left:
                break

            print((left, right))
            result += pow(2, right - left)

            left += 1

        return result % (10**9 + 7)
        

