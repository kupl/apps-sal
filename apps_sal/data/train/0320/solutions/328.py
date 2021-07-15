class Solution:
    def minOperations(self, nums: List[int]) -> int:
        big = 0
        ans = 0
        for i in range(len(nums)):
            twos = 0
            while nums[i] > 0:
                if nums[i] % 2 == 0:
                    twos += 1
                    nums[i] = nums[i] // 2
                else:
                    ans += 1
                    nums[i] -= 1
                
            if twos > big:
                big = twos
        return ans + big
