class Solution:
    def minDifference(self, nums: List[int]) -> int:
        l = nums[::]
        l.sort()
        if len(l) <= 4:
            return 0
        else:
            return min(abs(l[-4] - l[0]), abs(l[-1] - l[3]), abs(l[2] - l[-2]), abs(l[-3] - l[1]))
