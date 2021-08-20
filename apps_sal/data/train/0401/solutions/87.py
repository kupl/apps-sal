class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        mod = [0, -1, -1]
        mod[nums[0] % 3] = nums[0]
        for i in range(1, len(nums)):
            mod2 = list(mod)
            for j in range(3):
                if mod[j] != -1:
                    newSum = mod[j] + nums[i]
                    mod2[newSum % 3] = max(mod[newSum % 3], newSum)
            mod = mod2
        return mod[0] if mod[0] != -1 else 0
