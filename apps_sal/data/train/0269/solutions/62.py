class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        p = -1000000
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                if i-p-1 >= k:
                    p = i
                else:
                    return False
        return True
