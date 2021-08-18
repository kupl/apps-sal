class Solution:
    count = 0

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        comb = [0] * (target + 1)
        comb[0] = 1
        for i in range(1, len(comb)):
            for j in range(0, len(nums)):
                if i - nums[j] >= 0:
                    comb[i] += comb[i - nums[j]]
        return comb[target]
