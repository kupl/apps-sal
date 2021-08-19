import math


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        max_log = 0
        count_zero = 0
        steps = 0
        for num in nums:
            if num != 0:
                log_num = 0
                while num > 0:
                    if num % 2 == 0:
                        num /= 2
                        log_num += 1
                    else:
                        steps += 1
                        num -= 1
                max_log = max(max_log, log_num)
        return steps + max_log
