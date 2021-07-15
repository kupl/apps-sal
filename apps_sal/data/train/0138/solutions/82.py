class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] > 0:
                nums[i] = 2
            elif nums[i] < 0:
                nums[i] = -2
        mini, maxi, res = 1, 1, -10**9 - 1
        for n in nums:
            a = mini * n
            b = maxi * n
            mini = min(a,b,n)
            maxi = max(a,b,n)
            res = max(res, maxi)
        if res <= 0:
            return 0
        return int(math.log2(res))

