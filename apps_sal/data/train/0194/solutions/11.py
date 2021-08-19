class Solution:

    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = sum(nums)
        if total % k != 0:
            return False
        subsetTotal = total // k
        visited = [0] * len(nums)
        return self.helper(k, 0, 0, visited, nums, k, subsetTotal)

    def helper(self, remainingSets, index, s, visited, nums, k, subsetTotal):
        if remainingSets == 1:
            return True
        if s == subsetTotal:
            return self.helper(remainingSets - 1, 0, 0, visited, nums, k, subsetTotal)
        for i in range(index, len(nums)):
            if visited[i] == 0 and s + nums[i] <= subsetTotal:
                visited[i] = 1
                if self.helper(remainingSets, i + 1, s + nums[i], visited, nums, k, subsetTotal):
                    return True
                visited[i] = 0
        return False
