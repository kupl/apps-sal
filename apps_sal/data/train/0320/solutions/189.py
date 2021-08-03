class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = max_mult = 0
        for num in nums:
            count = 0
            while num != 0:
                if num % 2:
                    res += 1
                    num -= 1
                else:
                    count += 1
                    num //= 2
            max_mult = max(max_mult, count)

        return res + max_mult
