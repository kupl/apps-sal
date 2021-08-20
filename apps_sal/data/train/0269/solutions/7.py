class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        p = 0
        count = k + 1
        while p < len(nums):
            if nums[p] == 1:
                if count <= k:
                    return False
                else:
                    count = 0
            count += 1
            p += 1
        return True
