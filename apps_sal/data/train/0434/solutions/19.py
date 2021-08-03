class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mc = 0
        onep = False
        for i in range(len(nums)):
            if nums[i] == 0:
                c = 0
                j = i - 1
                while j >= 0 and nums[j] != 0:
                    j -= 1
                    c += 1

                j = i + 1
                while j < len(nums) and nums[j] != 0:
                    j += 1
                    c += 1

                if c > mc:
                    mc = c
            else:
                onep = True

        if onep and mc == 0:
            return len(nums) - 1

        elif not onep and mc == 0:
            return 0
        else:
            return mc
