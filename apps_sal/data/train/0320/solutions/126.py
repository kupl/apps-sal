class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def get_add_mul_times(num: int):
            a, b = 0, 0
            while num > 0:
                if num >> 1 << 1 != num:
                    a += 1
                    num -= 1
                else:
                    b += 1
                    num //= 2
            return a, b
        N = len(nums)
        add, mul = [0] * N, [0] * N
        for ii in range(N):
            a, b = get_add_mul_times(nums[ii])
            add[ii] = a
            mul[ii] = b
        return max(mul) + sum(add)
