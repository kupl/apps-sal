class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        result = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                result.append(sum(nums[i:j + 1]))
        result.sort()
        return sum(result[left - 1:right]) % (10 ** 9 + 7)
