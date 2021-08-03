import math


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        max_half_ops = 0

        def find_odd_ops_req(num):
            nonlocal max_half_ops
            result = 0
            half_ops = 0
            while(num):
                result += num & 1
                half_ops += 1
                num = num >> 1
            max_half_ops = max(max_half_ops, half_ops - 1)
            return result

        result = 0
        for num in nums:
            result += find_odd_ops_req(num)
        return result + max_half_ops
