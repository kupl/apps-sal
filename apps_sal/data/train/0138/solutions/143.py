class Solution:

    def getMaxLen(self, nums: List[int]) -> int:

        def conv(n):
            if n > 0:
                return 1
            if n == 0:
                return 0
            return -1
        nums = list(map(conv, nums))
        n = len(nums)

        def check(size):
            if size == 0:
                return True
            if size > n:
                return False
            p = 1
            lo = hi = 0
            while hi < n:
                if nums[hi] == 0:
                    p = 1
                    lo = hi = hi + 1
                    continue
                p *= nums[hi]
                if hi - lo + 1 == size:
                    if p > 0:
                        return True
                    p //= nums[lo]
                    lo += 1
                hi += 1
            return False
        res = 0
        (lo, hi) = (0, n)
        while lo <= hi:
            m = (lo + hi) // 2
            (r1, r2) = (check(m), check(m + 1))
            if r1 or r2:
                if r1:
                    res = m
                if r2:
                    res = m + 1
                lo = m + 2
            else:
                hi = m - 1
        return res
