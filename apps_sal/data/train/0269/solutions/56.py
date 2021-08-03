class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if nums.count(1) == 0:
            return True

        c = []
        for i in range(len(nums)):
            if nums[i] == 1:
                c.append(i)

        for i in range(1, len(c)):
            if c[i] - c[i - 1] <= k:
                return False
        return True
