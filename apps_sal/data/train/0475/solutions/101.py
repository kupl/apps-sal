class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        result = []
        result.append(nums[0])
        for i in range(1, n):
            result.append(nums[i])
            nums[i] += nums[i - 1]
            result.append(nums[i])
            for j in range(i - 1):
                result.append(nums[i] - nums[j])
        result.sort()
        return sum(result[left - 1:right]) % 1000000007
