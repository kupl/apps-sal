class Solution:
    def minOperations(self, nums: List[int]) -> int:
        max_mul = 0
        total_add = 0
        ope_dict = {0: (0, 0)}
        def func(num: int):
            if num in ope_dict:
                return ope_dict[num]
            elif num % 2:
                r = func(num - 1)
                ope_dict[num] = (r[0] + 1, r[1])
            else:
                r = func(num // 2)
                ope_dict[num] = (r[0], r[1] + 1)
            return ope_dict[num]
        for n in nums:
            add, mul = func(n)
            total_add += add
            max_mul = max(max_mul, mul)
        return total_add + max_mul
            

