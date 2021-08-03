class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op_0, op_1 = 0, 1
        for num in nums:
            b_len = 0
            while num:
                op_0 += num & 1
                num >>= 1
                b_len += 1
            op_1 = max(op_1, b_len)
        return op_0 + op_1 - 1
