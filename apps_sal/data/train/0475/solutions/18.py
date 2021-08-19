class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        n = len(nums)
        prefix = [0 for i in range(n + 1)]
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        for k in range(2, n + 1):
            for i in range(n - k + 1):
                nums.append(prefix[i + k] - prefix[i])
        nums.sort()
        t = 1000000007
        ans = 0
        for i in range(left, right + 1):
            ans = (nums[i - 1] % t + ans % t) % t
        return ans
