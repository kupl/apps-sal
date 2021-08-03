class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        while True:
            count = 0
            flag = 0
            for i in range(len(nums)):
                if nums[i] & 1:
                    count += 1
                    nums[i] -= 1
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] = nums[i] // 2
                    flag = 1
            ans += count
            if flag:
                ans += 1
            count = 0
            if nums.count(0) == len(nums):
                return ans
