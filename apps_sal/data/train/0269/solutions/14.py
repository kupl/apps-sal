class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = 0
        while prev < len(nums) and nums[prev] == 0:
            prev += 1
        if prev == len(nums) or nums[prev] == 0:
            return True
        if k == 0:
            return True

        for i in range(prev + 1, len(nums)):
            if nums[i] == 1:
                if i - prev <= k:
                    return False
                prev = i
        return True
