class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        result = 0
        pre_sum = [0] * (n + 1)
        for (i, num) in enumerate(nums):
            pre_sum[i + 1] = pre_sum[i] + num
        seen = {0: 0}
        for i in range(1, n + 1):
            cur = pre_sum[i]
            if cur - target in seen:
                result += 1
                seen = {}
            seen[cur] = i
        return result
