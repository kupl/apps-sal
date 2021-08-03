class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prevStart = -1
        candidates = []
        if 0 not in nums:
            return len(nums) - 1
        for i in range(len(nums)):
            if nums[i] == 1:
                if prevStart == -1:
                    prevStart = i
                    continue
            else:
                if prevStart != -1:
                    candidates.append([prevStart, i - 1])
                    prevStart = -1
        if prevStart != -1:
            candidates.append([prevStart, len(nums) - 1])

        res = [0]
        for i in range(len(candidates)):
            if i == len(candidates) - 1:
                res.append(candidates[i][1] - candidates[i][0] + 1)
            else:
                if candidates[i + 1][0] - candidates[i][1] == 2:
                    res.append(candidates[i + 1][1] - candidates[i][0])
                else:
                    res.append(candidates[i][1] - candidates[i][0] + 1)
        return max(res)
