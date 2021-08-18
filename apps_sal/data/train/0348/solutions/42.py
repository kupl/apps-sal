class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        maxi = nums[0]
        sumi = nums[0]
        left = [nums[0]]
        right = [nums[-1]]
        for i in nums[1:]:
            sumi = max(i, sumi + i)
            left.append(sumi)
        t = nums[::-1]
        sumi = t[0]
        for i in t[1:]:
            sumi = max(i, sumi + i)
            right.append(sumi)
        right = right[::-1]
        l = len(nums)
        res = 0
        for i in range(l):
            res = max(res, (left[i] + right[i] - (2 * nums[i])))
        if res != 0:
            return res
        return max(nums)
