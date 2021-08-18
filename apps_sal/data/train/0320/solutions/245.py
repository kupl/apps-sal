class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        big = 0

        for i in range(len(nums)):
            k = nums[i]
            k = bin(k)
            ans += k.count('1')
            big = max(big, 0, len(k) - 3)

        ans += big

        return ans
