class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums) == 0:
            return 0
        dec_stack = []
        inc_stack = []
        max_interval = 1

        l, r = 0, 0
        min_v, max_v = nums[0], nums[0]
        dec_stack.append((nums[0], 0))
        inc_stack.append((nums[0], 0))

        while l < len(nums) and r < len(nums):
            while max_v - min_v <= limit:
                max_interval = max(max_interval, r - l + 1)
                r += 1
                if r == len(nums):
                    break
                while dec_stack and nums[r] > dec_stack[-1][0]:
                    dec_stack.pop(-1)
                dec_stack.append((nums[r], r))
                max_v = dec_stack[0][0]

                while inc_stack and nums[r] < inc_stack[-1][0]:
                    inc_stack.pop(-1)
                inc_stack.append((nums[r], r))
                min_v = inc_stack[0][0]

            while max_v - min_v > limit:
                if dec_stack[0][1] == l:
                    dec_stack.pop(0)
                    max_v = dec_stack[0][0]
                if inc_stack[0][1] == l:
                    inc_stack.pop(0)
                    min_v = inc_stack[0][0]
                l += 1

        return max_interval
