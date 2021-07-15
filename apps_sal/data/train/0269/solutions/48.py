class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i, j,  d=  float('-inf'), 0, float('inf')
        while j <len(nums):
            if nums[j]:
                d = min(d, j-i-1)
                if d<k:
                    return False
                i = j
            j+=1
        return True
