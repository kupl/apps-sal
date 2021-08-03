class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        flag = True
        n = len(nums)
        while flag:
            flag = False
            for i in range(n):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    ans += 1
                if nums[i] != 0:
                    flag = True
            if flag:
                for i in range(n):
                    nums[i] /= 2
                ans += 1
        return ans
