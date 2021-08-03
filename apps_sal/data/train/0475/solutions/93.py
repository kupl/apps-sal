class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        import functools
        sums = []

        for i in range(len(nums)):
            temp = 0
            for j in range(i, len(nums)):
                temp += nums[j]
                sums.append(temp)

        sums.sort()
        return (functools.reduce(lambda x, y: x + y, sums[left - 1:right])) % (7 + 10**9)
