class Solution:

    def minOperations(self, nums: List[int]) -> int:
        (x, y) = (0, 0)
        for num in nums:
            num = format(num, 'b')
            x += num.count('1')
            y = max(y, len(num) - 1)
        return x + y
