import math


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        power = [0] * n
        rem = [0] * n
        for i in range(n):
            j = nums[i]
            count1 = 0
            count2 = 0
            while j > 0:
                if j % 2 == 0:
                    count1 += 1
                    j = j // 2
                else:
                    count2 += 1
                    j = j - 1
            power[i], rem[i] = count1, count2
        ans = max(power) + sum(rem)
        return ans
