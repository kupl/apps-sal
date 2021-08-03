class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxd = []
        mind = []
        left = 0
        sol = 1
        for i, num in enumerate(nums):
            while maxd and nums[maxd[-1]] < num:
                maxd.pop()
            while mind and nums[mind[-1]] > num:
                mind.pop()
            maxd.append(i)
            mind.append(i)
            while nums[maxd[0]] - nums[mind[0]] > limit:
                if nums[maxd[0]] == nums[left]:
                    maxd.pop(0)
                if nums[mind[0]] == nums[left]:
                    mind.pop(0)
                left += 1
            sol = max(sol, i - left + 1)
            # print(maxd,mind,sol,left)
        return sol
