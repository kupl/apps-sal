class Solution:
    def minOperations(self, nums: List[int]) -> int:
        a = m = 0
        for i in nums:
            a += bin(i).count('1')
            m = max(m, len(bin(i)) - 3)
        return a + m
