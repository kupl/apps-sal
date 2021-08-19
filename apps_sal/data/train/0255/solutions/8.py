class Solution:

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) <= 1:
            return 0
        start = currEnd = nextEnd = jump = 0
        while currEnd - start + 1 > 0:
            jump += 1
            for i in range(start, currEnd + 1):
                nextEnd = max(nums[i] + i, nextEnd)
                if nextEnd >= len(nums) - 1:
                    return jump
            start = currEnd + 1
            currEnd = nextEnd
        return jump
