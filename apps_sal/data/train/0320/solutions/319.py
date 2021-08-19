class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        s = sum(nums)
        while s != 0:
            nums_2 = [num % 2 for num in nums]
            diff = sum(nums_2)
            if diff == 0:
                nums = [num // 2 for num in nums]
                ans += 1
                s //= 2
            else:
                ans += diff
                s -= diff
                nums = [nums[i] - nums_2[i] for i in range(n)]
        return ans
