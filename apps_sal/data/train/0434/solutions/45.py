class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 0
        if 0 not in nums:
            return len(nums) - 1
        new = []
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == 1:
                cnt = 0
                while i < n and nums[i] == 1:
                    cnt += 1
                    i += 1
                new.append(cnt)
            else:
                new.append(0)
                i += 1
        mx = max(new)
        for i in range(1, len(new) - 1):
            if new[i] == 0:
                mx = max(mx, new[i - 1] + new[i + 1])
        return mx
