class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        deleted = False
        max_, cur_cnt, last_cnt = 0, 0, 0
        idx, size = 0, len(nums)

        while idx < size and nums[idx] == 0:
            idx += 1
        for i in range(idx, size):
            if nums[i] == 1:
                cur_cnt += 1
                max_ = max(max_, cur_cnt)
            else:
                if not deleted:
                    deleted = True
                else:
                    cur_cnt -= last_cnt
                last_cnt = cur_cnt

        if size == sum(nums):
            return size - 1  # [1,1,1,1]
        return max_
