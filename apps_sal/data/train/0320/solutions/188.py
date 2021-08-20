class Solution:

    def minOperations(self, nums: List[int]) -> int:
        n = m = 0
        for x in nums:
            s = bin(x)[2:]
            m = max(len(s) - 1, m)
            n += len(s.replace('0', ''))
        return m + n
