class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        while any(nums):
            temp = [0] * len(nums)
            flag = False
            for i in range(len(nums)):
                if nums[i] % 2:
                    nums[i] -= 1
                    flag = True
                    ans += 1
                elif not flag and not nums[i] % 2:
                    temp[i] = nums[i] // 2
            if not flag:
                ans += 1
                nums = temp
            # print(nums)
        return ans
