class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        num_zero = sum((n == 0 for n in nums))
        while num_zero != len(nums):
            for (i, n) in enumerate(nums):
                if n % 2 == 1:
                    ans += 1
                    nums[i] -= 1
                    if nums[i] == 0:
                        num_zero += 1
                nums[i] >>= 1
            ans += 1
        return ans - 1

    def num_steps(self, n):
        if n == 0:
            return 0
        (steps, mask) = (0, 1)
        while mask <= n:
            if n & mask:
                steps += 2
            else:
                steps += 1
            mask <<= 1
        return steps - 1
