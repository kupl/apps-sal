class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if all(nums):
            return len(nums)-1
        m = pre = l = pl = 0
        for i, n in enumerate(nums):
            if n == pre == 1:
                l += 1
            elif n == pre == 0:
                pl = 0
            elif n == 1 != pre:
                l = 1
            else:
                m = max(m, pl + l)
                pl = l
            pre = n
        return max(m, pl + l) if pre == 1 else m
