class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        front, end = 0, 0
        tot = 0
        output = 0
        ct = 0
        while end < len(nums):
            if 1 & nums[end]:
                tot += 1
                ct = 0
            end += 1
            while tot == k:
                tot -= nums[front] & 1
                front += 1
                ct += 1
            output += ct
        return output
