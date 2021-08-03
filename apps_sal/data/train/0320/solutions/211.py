class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        while any([True if num > 0 else False for num in nums]):
            for idx, num in enumerate(nums):
                if num % 2 == 1:
                    ans += 1
                    nums[idx] -= 1
            flag = 0
            for idx, num in enumerate(nums):
                if num != 0:
                    flag = True
                    nums[idx] = num // 2
            if flag:
                ans += 1
        return ans
