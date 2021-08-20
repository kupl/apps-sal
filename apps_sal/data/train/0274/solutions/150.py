class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        根据要求，子串任意两个数之间的差要小于等于limit
        所以利用递增栈与递减栈记录子串的最大与最小值
        maxs[0]-mins[0] 作为子数组的最大maxdiff
        """
        n = len(nums)
        maxs = []
        mins = []
        l = res = 0
        for r in range(n):
            while maxs and maxs[-1] < nums[r]:
                maxs.pop()
            maxs.append(nums[r])
            while mins and mins[-1] > nums[r]:
                mins.pop()
            mins.append(nums[r])
            while maxs[0] - mins[0] > limit:
                if maxs[0] == nums[l]:
                    maxs.pop(0)
                if mins[0] == nums[l]:
                    mins.pop(0)
                l += 1
            res = max(res, r - l + 1)
        return res
