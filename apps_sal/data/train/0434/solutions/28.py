class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        (l, r) = ([0] * n, [0] * n)
        for i in range(1, n):
            l[i] = l[i - 1] + 1 if nums[i - 1] == 1 else 0
        for i in range(n - 2, -1, -1):
            r[i] = r[i + 1] + 1 if nums[i + 1] == 1 else 0
        ans = max(r[0], l[n - 1])
        for i in range(1, n - 1):
            ans = max(ans, l[i] + r[i])
        return ans
