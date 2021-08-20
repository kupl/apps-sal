class Solution:

    def minOperations(self, nums: List[int]) -> int:
        res = sum((num > 0 for num in nums))
        max_time = 0
        for num in nums:
            add_op = 0
            time_op = 0
            Y = num
            X = 1
            while Y > X:
                if Y % 2 == 1:
                    Y -= 1
                    add_op += 1
                else:
                    Y /= 2
                    time_op += 1
            max_time = max(max_time, time_op)
            if num > 1:
                res += add_op
        res += max_time
        return res
