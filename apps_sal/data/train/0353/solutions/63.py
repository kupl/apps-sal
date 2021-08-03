class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0
        right_boundary = len(nums) - 1
        for index, num in enumerate(nums):
            if num * 2 > target:
                break
            left = index
            right = right_boundary
            while left < right:
                mid = (left + right + 1) // 2
                if nums[mid] + num <= target:
                    left = mid
                else:
                    right = mid - 1
            right_boundary = left
            tail_length = right_boundary - index
            result += 1 << tail_length
            result %= 10 ** 9 + 7

        return result
