class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        res = 0
        logs = []
        for x in nums:
            if x == 0:
                logs.append(res)
                res = 0
            else:
                res += 1
        logs.append(res)
        if len(logs) == 1:
            return max(0, logs[0] - 1)
        return max([logs[i] + logs[i + 1] for i in range(len(logs) - 1)])
