class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        before = -k - 5
        for i in range(len(nums)):
            if nums[i] == 1:
                if i - before <= k:
                    return False
                before = i
        return True
