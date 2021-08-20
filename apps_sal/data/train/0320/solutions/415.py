class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        while set(nums) != {0}:
            even = True
            for i in range(len(nums)):
                if nums[i] & 1:
                    ans += 1
                    even = False
                    nums[i] -= 1
            if even:
                nums = [i // 2 for i in nums]
                ans += 1
        return ans
