class Solution:

    def getMaxLen(self, nums: List[int]) -> int:

        def _getMaxLen(nums):
            if not nums:
                return 0
            n_ones = sum(nums)
            if n_ones % 2 == 0:
                return len(nums)
            return len(nums) - min(nums.index(1), nums[::-1].index(1)) - 1
        ans = prev = 0
        nums = [0 if i > 0 else 1 if i < 0 else -1 for i in nums]
        while nums:
            try:
                idx = nums.index(-1)
                ans = max(_getMaxLen(nums[:idx]), ans)
                nums = nums[idx + 1:]
            except:
                ans = max(ans, _getMaxLen(nums))
                break
        return ans
