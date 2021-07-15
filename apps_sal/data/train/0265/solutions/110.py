class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        seen = {0: -1}
        prev = -1
        count = 0
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            if nums[i] == target or (curr - target in seen and prev < seen[curr - target] + 1):
                prev = i
                count += 1
            seen[curr] = i
        return count

