class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        a = []

        for i in range(len(nums)):
            total = nums[i]
            a.append(total)
            for j in range(i + 1, len(nums)):
                total += nums[j]
                a.append(total)

        a.sort()

        return sum(a[left - 1:right]) % 1_000_000_007
