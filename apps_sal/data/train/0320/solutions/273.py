class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        cnt = len(nums)
        for n in nums:
            if n == 0:
                cnt -= 1
        while cnt > 0:
            for i, n in enumerate(nums):
                if n != 0 and n % 2 == 1:
                    nums[i] -= 1
                    ans += 1
                    if nums[i] == 0:
                        cnt -= 1
            two = 0
            for i, n in enumerate(nums):
                if n != 0 and n % 2 == 0:
                    two = 1
                    nums[i] //= 2
            ans += two
        return ans
