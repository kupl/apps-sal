from math import ceil


def is_fine(nums, val, threshold):
    tot = 0
    for i in nums:
        tot += ceil(i / val)
    if tot <= threshold:
        return True
    else:
        return False


def bSearch(l, r, nums, threshold):
    if l <= r:
        mid = (l + r) // 2
        high_val = is_fine(nums, mid, threshold)
        low_val = is_fine(nums, mid - 1, threshold)
        if high_val is True and low_val is False:
            return mid
        elif high_val is False and low_val is False:
            return bSearch(mid + 1, r, nums, threshold)
        else:
            return bSearch(l, mid - 1, nums, threshold)
    else:
        return None


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if sum(nums) <= threshold:
            return 1
        return bSearch(2, 10**6, nums, threshold)
