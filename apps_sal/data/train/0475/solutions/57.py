MAX = 10 ** 9 + 7


class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subs = subarrays(nums, n)
        subs.sort()
        return sum(subs[left - 1:right]) % MAX


def subarrays(nums: List[int], n: int) -> List[int]:
    r = []
    for i in range(0, len(nums)):
        for j in range(i + 1, min(i + n, len(nums)) + 1):
            r.append(sum(nums[i:j]))
    return r
