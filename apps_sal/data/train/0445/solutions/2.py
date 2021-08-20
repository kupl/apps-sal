class Solution:

    def minDifference(self, nums: List[int]) -> int:
        a = nums
        if len(a) <= 4:
            return 0
        a.sort()
        print(a)
        return min(a[-1] - a[3], a[-2] - a[2], a[-3] - a[1], a[-4] - a[0])
