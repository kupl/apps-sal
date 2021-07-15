class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        vals = [0]*(len(nums)-1)
        for i, n in enumerate(nums[1:]):
            vals[i] = abs(n-nums[i])
        base = sum(vals)
        bonus = 0

        MPP = max(nums[L]+nums[L+1]-vals[L] for L in range(len(nums)-1))
        MPN = max(nums[L]-nums[L+1]-vals[L] for L in range(len(nums)-1))
        MNP = max(-nums[L]+nums[L+1]-vals[L] for L in range(len(nums)-1))
        MNN = max(-nums[L]-nums[L+1]-vals[L] for L in range(len(nums)-1))

        bonus = max(MPP+MNN, MPN+MNP)

        for R in range(0, len(nums)-1):
            bonus = max(bonus, abs(nums[0]-nums[R+1]) - vals[R])

        for L in range(1, len(nums)-1):
            bonus = max(bonus, abs(nums[L-1]-nums[len(nums)-1]) - vals[L-1])

        return base+bonus
