class Solution:

    def minOperations(self, nums: List[int]) -> int:
        count = 0
        max_max_power = 0
        for n in nums:
            if n == 0:
                continue
            max_power = 0
            temp = n
            while temp > 1:
                max_power += 1
                temp >>= 1
            max_max_power = max(max_max_power, max_power)
            while max_power >= 0:
                if 2 ** max_power <= n:
                    n -= 2 ** max_power
                    count += 1
                max_power -= 1
        return count + max_max_power
