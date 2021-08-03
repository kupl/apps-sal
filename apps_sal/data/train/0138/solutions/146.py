class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def _getMaxLen(nums):
            if not nums:
                return 0
            fn = 0
            while fn < len(nums) and nums[fn] > 0:
                fn += 1
            pos = True
            res = 0
            for i in range(len(nums)):
                if nums[i] < 0:
                    pos = not pos
                if pos:
                    res = max(res, i + 1)
                else:
                    res = max(res, i - fn)
            return res
        ans = prev = 0
        while nums:
            try:
                idx = nums.index(0)
                ans = max(_getMaxLen(nums[:idx]), ans)
                nums = nums[idx + 1:]
            except:
                ans = max(ans, _getMaxLen(nums))
                break
        return ans
