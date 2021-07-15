class Solution:
    def maxNonOverlapping(self, nums, target):
        ans = 0
        cur = 0
        tmp = set([0])
        for n in nums:
            cur += n
            if cur - target in tmp:
                ans += 1
                cur = 0
                tmp = set([0])
            tmp.add(cur)
        return ans
