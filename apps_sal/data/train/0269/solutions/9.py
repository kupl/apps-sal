class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        s = -1
        e = -1
        n = len(nums)
        for i in range(n):
            if nums[i] == 1 and s == -1:
                s = i
            elif nums[i] == 1:
                e = i
                interval = e - s - 1
                if interval < k:
                    return False
                s = i
        return True
