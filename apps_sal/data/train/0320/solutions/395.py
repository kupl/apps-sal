class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = 0

        while nums:
            new = []
            for x in nums:
                if x > 0:
                    if x != 1:
                        new.append(x - (x&1))
                    result += x&1
            nums = new
            
            if not nums:
                break
            
            for i in range(len(nums)):
                nums[i] //= 2
            result += 1
            
        return result
