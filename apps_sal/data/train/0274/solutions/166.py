class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        incr_q = [nums[0]]
        decr_q = [nums[0]]
        res = 1
        left = 0
        right = 1
        while right < len(nums):
            while incr_q and incr_q[-1] > nums[right]:
                incr_q.pop()
            incr_q.append(nums[right])
            while decr_q and decr_q[-1] < nums[right]:
                decr_q.pop()
            decr_q.append(nums[right])
            while incr_q and decr_q and (decr_q[0] - incr_q[0] > limit):
                if nums[left] == incr_q[0]:
                    incr_q.pop(0)
                if nums[left] == decr_q[0]:
                    decr_q.pop(0)
                left += 1
            res = max(right - left + 1, res)
            right += 1
        return res
