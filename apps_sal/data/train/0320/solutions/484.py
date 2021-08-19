class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        mx = 0
        for n in nums:
            b = bin(n)
            ans += b.count('1')
            mx = max(mx, len(b) - 3)
        return ans + mx
