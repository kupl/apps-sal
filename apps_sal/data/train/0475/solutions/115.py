class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # two pointer approach?
        sums = []
        for L in range(len(nums)):
            prefix = 0
            start = L
            while(start < len(nums)):
                prefix += nums[start]
                sums.append(prefix)
                start += 1
        sums.sort()
        # print(sums)
        return sum(sums[left - 1:right]) % (10**9 + 7)
