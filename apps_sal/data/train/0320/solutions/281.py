class Solution:

    def minOperations(self, nums: List[int]) -> int:
        val = max(nums)
        double = 0
        add = 0
        value = 0
        count = 0
        value = val
        while value != 0:
            if value % 2 == 0:
                value = value // 2
                double += 1
            else:
                value -= 1
                add += 1
        count += double
        print(add, double)
        for x in nums:
            value = x
            half = 0
            add = 0
            while value != 0:
                if value % 2 == 0:
                    value = value // 2
                    half += 1
                else:
                    value -= 1
                    add += 1
            count += add
        return count
