class Solution:
    def minOperations(self, nums: List[int]) -> int:
        goal = [0]*len(nums)
        if nums == goal:
            return 0 
        calls = 0 
        div_needed = False
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums[i] -= 1
                calls += 1
            if nums[i] > 0:
                div_needed = True
        if div_needed:
            nums = [n/2 for n in nums]
            calls += 1
        return calls + self.minOperations(nums)
