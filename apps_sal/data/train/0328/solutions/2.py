class Solution:

    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        s2_candidate = [nums[-1]]
        cur_idx = len(nums) - 2
        while cur_idx >= 0 and nums[cur_idx] <= s2_candidate[-1]:
            s2_candidate.append(nums[cur_idx])
            cur_idx -= 1
        if cur_idx < 0:
            return False
        s3 = nums[cur_idx]
        while s2_candidate and s2_candidate[-1] < s3:
            s2 = s2_candidate.pop()
        cur_idx -= 1
        while cur_idx >= 0:
            if nums[cur_idx] < s2:
                return True
            elif nums[cur_idx] >= s3:
                if nums[cur_idx] > s3:
                    s2 = s3
                s3 = nums[cur_idx]
                while s2_candidate and s2_candidate[-1] <= s3:
                    next_s2 = s2_candidate.pop()
                    if next_s2 > s2 and next_s2 < s3:
                        s2 = next_s2
            elif nums[cur_idx] < s3 and nums[cur_idx] > s2:
                s2_candidate.append(nums[cur_idx])
            cur_idx -= 1
        return False
