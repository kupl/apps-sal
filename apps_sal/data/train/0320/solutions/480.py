class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ans = max_op = 0
        for b in map(bin, nums):
            ans += b.count('1')
            max_op = max(max_op, len(b) - 3)
        return ans + max_op
