class Solution:

    def minOperations(self, nums: List[int]) -> int:
        total = 0
        max_divide = 0
        for (i, x) in enumerate(nums):
            divide = 0
            while x > 0:
                if x % 2 == 1:
                    x -= 1
                    total += 1
                else:
                    x /= 2
                    divide += 1
            if divide > max_divide:
                max_divide = divide
        return total + max_divide
