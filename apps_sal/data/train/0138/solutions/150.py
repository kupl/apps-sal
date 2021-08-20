class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        zeroIdx = []
        for (idx, num) in enumerate(nums):
            if num == 0:
                zeroIdx += (idx,)
        start = 0
        ans = 0
        for idx in zeroIdx:
            if idx - start > 0:
                ans = max(ans, self.maxLength(nums, [start, idx], idx))
            start = idx + 1
        ans = max(ans, self.maxLength(nums, [start, len(nums)], len(nums)))
        return ans

    def maxLength(self, nums, arr, N):
        product = 1
        Len = 0
        for i in range(arr[0], arr[1]):
            product *= nums[i]
        if product >= 0:
            return arr[1] - arr[0]
        for i in range(arr[0], arr[1]):
            if nums[i] < 0:
                Len = max(Len, max(N - i - 1, i - arr[0]))
        return Len
