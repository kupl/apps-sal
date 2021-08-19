from collections import deque
'''
We need to figure out basically for k numbers remaining what is the largest sum, assuming that the first of those is selected.
'''


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        numLength = len(nums)
        maxSums = defaultdict(int)
        maxSum = nums[0]  # as that is definitely a lower bound on the maxSum, as that is obviously a possible sum. Be careful when you initialize mins and maxs
        maxQueue = deque([0])  # this will be used to compute the list of values of the maxSum for the previousk indices.
        for i in range(numLength - 1, -1, -1):
            ithMax = max(nums[i], maxQueue[0] + nums[i])  # be careful of index name.
            maxSums[i] = ithMax
            # print(\"Max Queue before popping: \",maxQueue)
            if len(maxQueue) == k:  # be careful of variables
                if maxSums[i + k] == maxQueue[0]:
                    maxQueue.popleft()  # this is needed to ensure that we don't have values that have expired.
            while maxQueue and ithMax > maxQueue[-1]:  # be sure of spelling and using right variables
                maxQueue.pop()
            maxQueue.append(ithMax)
            # print(\"Max Queue after popping: \",maxQueue)
            maxSum = max(ithMax, maxSum)
        return maxSum
