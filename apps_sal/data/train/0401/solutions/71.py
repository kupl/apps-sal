class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        l = [0] * 3
        for i in nums:
            t = [0] * 3
            for j in l:
                t[(j + i) % 3] = max(t[(j + i) % 3], j + i)
            for g in range(3):
                l[g] = max(t[g], l[g])
        return l[0]
