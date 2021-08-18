class Solution1:
    def minOperations(self, nums: List[int]) -> int:
        twos = 0
        ones = 0
        for n in nums:
            mul = 0
            while n:
                if n % 2:
                    n -= 1
                    ones += 1
                else:
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
                ans += n % 2
                nums[i] = n - n % 2
            if nums[idx] != 0:
                for i, n in enumerate(nums):
                    nums[i] = nums[i] // 2
                ans += 1

        return ans
