class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            ans += bin(x).count('1')
        width = len(bin(max(nums))) - 2

        return ans + width - 1
