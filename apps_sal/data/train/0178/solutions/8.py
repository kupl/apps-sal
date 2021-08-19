class Solution:

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        dp = []
        for i in nums:
            if not dp:
                dp.append(i)
            pos = self.search(i, dp)
            if pos == len(dp):
                dp.append(i)
            else:
                dp[pos] = i
            maxLen = max(maxLen, len(dp))
        return maxLen

    def search(self, curr, nums):
        start = 0
        end = len(nums) - 1
        if curr > nums[-1]:
            return len(nums)
        while end >= start:
            mid = int(start + (end - start) / 2)
            if curr < nums[mid]:
                end = mid - 1
            elif curr > nums[mid]:
                start = mid + 1
            else:
                return mid
        return start
