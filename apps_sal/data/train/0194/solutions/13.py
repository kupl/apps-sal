class Solution:

    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k <= 0:
            return False
        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False
        visited = [False] * len(nums)
        nums.sort(reverse=True)
        return self.canPartition(nums, visited, k, 0, 0, nums_sum / k)

    def canPartition(self, nums, visited, k, currentIndex, currentSum, target):
        if k == 1:
            return True
        if currentSum == target:
            return self.canPartition(nums, visited, k - 1, 0, 0, target)
        for i in range(currentIndex, len(nums)):
            if visited[i] is False and currentSum + nums[i] <= target:
                visited[i] = True
                if self.canPartition(nums, visited, k, i + 1, currentSum + nums[i], target):
                    return True
                visited[i] = False
        return False
