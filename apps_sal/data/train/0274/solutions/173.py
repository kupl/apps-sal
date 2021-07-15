class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums) == 0:
            return 0
        dec_stack = [] # stores all the next largest value  (value, pos)
        inc_stack = [] # stores all the next min value (value, pos)
        max_interval = 1
        
        # two pointer expand and contract, including
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
                # added new values update our stacks
                while dec_stack and nums[r] > dec_stack[-1][0]:
                    dec_stack.pop(-1)
                dec_stack.append((nums[r], r))
                max_v = dec_stack[0][0]
                
                while inc_stack and nums[r] < inc_stack[-1][0]:
                    inc_stack.pop(-1)
                inc_stack.append((nums[r], r))
                min_v = inc_stack[0][0]
            
            # now the interval does not fit the limit, contract
            while max_v - min_v > limit:
                if dec_stack[0][1] == l:
                    dec_stack.pop(0)
                    max_v = dec_stack[0][0]
                if inc_stack[0][1] == l:
                    inc_stack.pop(0)
                    min_v = inc_stack[0][0]
                l += 1
                
        return max_interval

