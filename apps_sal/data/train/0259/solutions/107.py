from math import ceil


def eval(nums, i, thold):
    s1 = 0
    for num in nums:
        s1 += ceil(num / i)
    if s1 <= thold:
        return True
    return False


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo, hi = 1, 100000000000
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if eval(nums, mid, threshold):
                hi = mid
            else:
                lo = mid + 1
        return lo
