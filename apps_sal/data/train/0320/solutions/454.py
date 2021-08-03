class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # [4, 2, 13]
        # 4 = 2^2
        # 2 = 2^1
        # 13 = 2^3 + 2^2 + 1 = 2^2(2 + 1) + 1
        # increment nums[2]
        # multiply by 2
        # increment nums[2] and nums[1]
        # multiply by 2
        # increment nums[1]
        # multiply by 2
        # total: 1 increment for each power of 2 in an element

        count = 0
        max_max_power = 0
        for n in nums:
            if n == 0:
                continue

            # get max power
            max_power = 0
            temp = n
            while temp > 1:
                max_power += 1
                temp >>= 1

            # record max max power
            max_max_power = max(max_max_power, max_power)

            # record digits of binary
            while max_power >= 0:
                if 2**max_power <= n:
                    n -= 2**max_power
                    count += 1
                max_power -= 1

        return count + max_max_power
