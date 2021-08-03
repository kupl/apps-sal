class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_step = 0
        last_step = 0
        i = 0
        n_jumps = 0
        while last_step < len(nums) - 1:
            while i <= last_step:
                current_step = max(i + nums[i], current_step)
                i += 1
            last_step = current_step
            n_jumps += 1
        return n_jumps
