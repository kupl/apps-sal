class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def calculate(num):
            temp1 = 0
            temp2 = 0
            while num:
                if num % 2:
                    temp1 += 1
                    num -= 1
                else:
                    temp2 += 1
                    num >>= 1

            return temp1, temp2

        ones, twos = 0, 0
        for val in nums:
            if val:
                a, b = calculate(val)
                ones += a
                twos = max(twos, b)
        print(ones)
        return ones + twos
