class Solution:
    def minOperations(self, nums: List[int]) -> int:

        res = 0
        while True:
            divide = False
            all_zero = True
            for i, n in enumerate(nums):
                if n == 0:
                    continue
                all_zero = False
                if n > 1:
                    divide = True
                res += n % 2
                nums[i] //= 2
            res += int(divide)
            if all_zero:
                break

        return res
