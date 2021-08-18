class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        result = 0
        for start in range(len(nums)):
            left, right = start, len(nums) - 1
            while left < right - 1:
                mid = (left + right) // 2
                if nums[mid] > target - nums[start]:
                    right = mid - 1
                else:
                    left = mid
            if nums[start] + nums[right] <= target:
                end = right
            elif nums[start] + nums[left] <= target:
                end = left
            elif nums[start] + nums[start] <= target:
                end = start
            else:
                end = -1
            if end > start:
                result += 2 ** (end - start)
            if end == start:
                result += 1
        return result % (10**9 + 7)
