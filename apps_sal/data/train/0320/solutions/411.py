class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        co = 0
        while True:
            co = 0
            for i in range(n):
                if nums[i] % 2 == 1:
                    nums[i]-=1
                    ans+=1
            for i in range(n):
                if nums[i] == 0:
                    co+=1
            if co==n:
                return ans
            for i in range(n):
                nums[i] = (nums[i] // 2)
            ans+=1
            # print(nums, ans, co)
            
        return ans
