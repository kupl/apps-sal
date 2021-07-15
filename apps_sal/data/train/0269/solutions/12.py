class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        next_one = 0
        previous_one = 0
        while(next_one < len(nums) and nums[next_one] != 1):
            next_one += 1
        if (next_one == len(nums)):
            return True
        previous_one = next_one
        next_one += 1
        
        while (next_one < len(nums)):
            while (next_one < len(nums) and nums[next_one] != 1):
                next_one += 1
            if (next_one < len(nums) and next_one - previous_one - 1 < k):
                return False
            elif (next_one < len(nums) and next_one - previous_one - 1 >= k):
                previous_one = next_one
            else:
                return True
            next_one += 1
        return True

