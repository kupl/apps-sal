class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = 0
        b = 0
        for n in nums:
            b += (f := f'{n:b}').count('1')
            s = max(s, len(f))
        return s - 1 + b

