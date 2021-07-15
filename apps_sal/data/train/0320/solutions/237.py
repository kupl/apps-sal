class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op1 = op2 = 0
        for num in nums:
            count1 = count2 = 0
            while num:
                if num & 1:
                    count1 += num & 1
                    num -= 1
                if num:
                    count2 += 1
                num >>= 1
            op1 += count1
            op2 = max(op2, count2)
        return op1 + op2
