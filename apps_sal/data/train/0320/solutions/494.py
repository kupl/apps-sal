class Solution:

    def minOperations(self, nums: List[int]) -> int:
        res = 0
        mul_max = 0
        for x in nums:
            if x == 0:
                continue
            x_bin = bin(x)
            mul = -1
            for i in x_bin[2:]:
                if i == '1':
                    res += 1
                mul += 1
            if mul > mul_max:
                mul_max = mul
        return res + mul_max
