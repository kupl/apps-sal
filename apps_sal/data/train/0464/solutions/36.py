class Solution:

    def minOperations(self, n: int) -> int:
        nums = [2 * i + 1 for i in range(n)]
        res = 0
        for i in range(n // 2):
            res += nums[n - 1 - i] - nums[i] >> 1
        return res
