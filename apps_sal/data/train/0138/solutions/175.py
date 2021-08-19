class Solution:

    def _getMaxLen(self, nums: List[int]) -> int:
        lz = [i for (i, v) in enumerate(nums) if v < 0]
        ts = len(nums)
        if len(lz) % 2 == 0:
            return ts
        if len(lz) == 1:
            lz = [lz[0], lz[0]]
        ls = lz[-1]
        rs = ts - (lz[0] + 1)
        if ls > rs:
            return ls
        return rs

    def getMaxLen(self, nums: List[int]) -> int:
        r = 0
        zero1 = 0
        try:
            zero1 = nums.index(0)
            r = self._getMaxLen(nums[:zero1])
            nums = nums[zero1 + 1:]
            while True:
                zero2 = nums.index(0)
                r2 = self._getMaxLen(nums[:zero2])
                if r2 > r:
                    r = r2
                zero1 = zero2
                nums = nums[zero1 + 1:]
        except ValueError:
            pass
        r2 = self._getMaxLen(nums)
        if r2 > r:
            r = r2
        return r
