class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                if i >= 1:
                    if count < k:
                        return False
                count = 0
            else:
                count += 1
        return True
