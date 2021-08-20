from collections import deque
'\nWe need to figure out basically for k numbers remaining what is the largest sum, assuming that the first of those is selected.\n'


class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        numLength = len(nums)
        maxSums = defaultdict(int)
        maxSum = nums[0]
        maxQueue = deque([0])
        for i in range(numLength - 1, -1, -1):
            ithMax = max(nums[i], maxQueue[0] + nums[i])
            maxSums[i] = ithMax
            if len(maxQueue) == k:
                if maxSums[i + k] == maxQueue[0]:
                    maxQueue.popleft()
            while maxQueue and ithMax > maxQueue[-1]:
                maxQueue.pop()
            maxQueue.append(ithMax)
            maxSum = max(ithMax, maxSum)
        return maxSum
