'''
[5,3,2,4]
[1,5,0,10,14]
[6,6,0,1,1,4,6]
[1,5,6,14,15]
'''


class Solution:
    def minDifference(self, nums: List[int]) -> int:

        n = len(nums)

        if n < 5:
            return 0

        nums.sort()

        diff = n - 4
        ans = math.inf
        for i in range(0, n - diff):
            ans = min(ans, nums[i + diff] - nums[i])

        return ans
