class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op = 0
        while sum(nums) != 0:
            odds = 0
            for i in range(len(nums)):
                if nums[i] & 1 != 0:
                    odds += 1
                    nums[i] -= 1
            if odds == 0:
                nums = list(map(lambda x: x // 2, nums))
                op += 1
            else:
                op += odds
                
        return op
