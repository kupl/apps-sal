class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = -k-1
        for i in range(len(nums)):
            if nums[i]:
                if i-last>k:
                    last = i
                else:
                    return False
        return True
