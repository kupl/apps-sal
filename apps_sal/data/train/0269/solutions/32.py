class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        left = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if left == -1:
                    left = i
                elif i - left - 1 < k:
                    return False
                else:
                    left = i
        return True
