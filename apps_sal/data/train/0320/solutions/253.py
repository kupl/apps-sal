class Solution1:
    def minOperations(self, nums: List[int]) -> int:
        twos = 0
        ones = 0
        for n in nums:
            mul = 0
            while n:
                if n % 2:  # odd number, just delete 1 so that it's now a multiple of 2
                    n -= 1
                    ones += 1
                else:  # multiple of 2, so just divide by 2
                    n //= 2
                    mul += 1
            twos = max(twos, mul)
        return ones + twos


class Solution:
    def minOperations(self, nums: List[int]) -> int:

        maxval = max(nums)
        idx = nums.index(maxval)
        ans = 0

        while nums[idx] != 0:
            for i, n in enumerate(nums):
                ans += n % 2  # minus 1 to make all number even
                nums[i] = n - n % 2
            if nums[idx] != 0:
                for i, n in enumerate(nums):  # devide all numbers by 2
                    nums[i] = nums[i] // 2
                ans += 1

        return ans
