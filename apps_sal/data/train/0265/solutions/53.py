class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        preSum = [0 for i in range(n + 1)]
        hashmap = {0: 0}
        lastend = 0
        ans = 0
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]
            begin = hashmap.get(preSum[i] - target, -1)
            if begin >= 0 and begin >= lastend:
                lastend = i
                ans += 1
            hashmap[preSum[i]] = i
        return ans
