class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        def find_right(nums, j, target):
            if j == 1:
                return j - 1
            i = 0
            while i < j:
                mid = i + (j - i) // 2
                if nums[mid] + nums[0] > target:
                    j = mid
                else:
                    i = mid + 1
            return i - 1

        n = len(nums)
        nums.sort()
        left = 0
        right = find_right(nums, len(nums), target)
        MOD = 10**9 + 7
        res = 0

        while left <= right:
            if nums[left] + nums[right] <= target:
                res = (res + pow(2, right - left)) % MOD
                left += 1
            else:
                right -= 1

        return res
