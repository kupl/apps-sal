class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True
        start = 0
        while start < len(nums) and nums[start] != 1:
            start += 1
        for i in range(start + 1, len(nums)):
            if nums[i] == 1:
                if i - start - 1 < k:
                    return False
                else:
                    start = i
        return True
