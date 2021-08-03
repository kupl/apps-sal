class Solution:
    def minOperations(self, nums: List[int]) -> int:
        add_count = sum(bin(v).count('1') for v in nums)
        mul_count = len(bin(max(nums))) - 3

        return add_count + mul_count

    def minOperations_my(self, nums: List[int]) -> int:
        add_sum = mul_maxi = 0
        for value in nums:
            c1 = c2 = 0
            while value > 1:
                if value & 1:
                    c1 += 1
                c2 += 1
                value >>= 1

            add_sum += c1 + value
            mul_maxi = max(mul_maxi, c2)

        return add_sum + mul_maxi
