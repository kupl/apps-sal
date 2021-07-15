class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i=0
        while i<len(nums):
            if nums[i]:
                break
            i+=1
        j=i
        i+=1
        while i<len(nums):
            if nums[i]:
                if i-j-1<k:
                    return False
                j=i
            i+=1
        return True

