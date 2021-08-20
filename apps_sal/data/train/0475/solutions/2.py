class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        for i in range(n):
            sums.append(nums[i])
            suma = nums[i]
            for j in range(i + 1, n):
                suma += nums[j]
                sums.append(suma)
        sums = sorted(sums)
        return sum(sums[left - 1:right]) % (10 ** 9 + 7)
