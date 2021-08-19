class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        l = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                l.append(sum(nums[i:j]))
        l.sort()
        return sum(l[left - 1:right]) % (10 ** 9 + 7)
