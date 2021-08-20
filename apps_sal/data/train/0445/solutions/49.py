class Solution:

    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        ns = sorted(nums)
        mindif = ns[-4] - ns[0]
        for i in range(1, 4):
            if ns[i - 4] - ns[i] < mindif:
                mindif = ns[i - 4] - ns[i]
        return mindif
