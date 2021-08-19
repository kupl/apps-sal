class Solution:

    def maxNonOverlapping(self, nums: list, target: int) -> int:
        sumDict = collections.defaultdict(collections.deque)
        preSum = 0
        sumDict[0].append(-1)
        right = -1
        ans = 0
        for i in range(len(nums)):
            preSum += nums[i]
            if preSum - target in sumDict:
                while sumDict[preSum - target] and sumDict[preSum - target][0] < right:
                    sumDict[preSum - target].popleft()
                if sumDict[preSum - target]:
                    ans += 1
                    right = i
            sumDict[preSum].append(i)
        return ans
