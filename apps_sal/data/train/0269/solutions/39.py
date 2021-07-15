class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        for idx in range(len(nums)):
            if nums[idx] == 1 and 1 in nums[idx+1:idx+k+1]:
                    return False
        return True

