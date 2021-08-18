

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = [sum(nums[i:j]) for i in range(len(nums) + 1) for j in range(i + 1, len(nums) + 1)]

        res.sort()
        return sum(res[left - 1:right]) % (10**9 + 7)


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        return sum(sorted([sum(nums[i:j]) for i in range(len(nums) + 1) for j in range(i + 1, len(nums) + 1)])[left - 1:right]) % (10**9 + 7)
