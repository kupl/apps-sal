class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:

        ind = 0
        for i, num in enumerate(nums):
            if not nums[ind] and num:
                ind = i
            if i != ind and num:
                if (i - ind) < (k + 1):
                    return False
                ind = i
        return True
            
        

