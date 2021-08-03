class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        tot = sum(nums)
        if k <= 0 or tot % k != 0:
            return False
        visited = [0] * len(nums)

        def canPart(nums, visited, idx, curSum, k, target):
            if k == 1:
                return True
            if curSum == target:
                return canPart(nums, visited, 0, 0, k - 1, target)
            if curSum > target:
                return False
            for i in range(idx, len(nums)):
                if not visited[i]:
                    visited[i] = 1
                    if canPart(nums, visited, i + 1, curSum + nums[i], k, target):
                        return True
                    visited[i] = 0
            return False

        return canPart(nums, visited, 0, 0, k, tot / k)
