class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        '''

        new array = [(st, curr_prod_from_st)]


        if curr_prod_from_st > 0:
            max_sub = max(max_sub, ed - st + 1) 
        elif:
            max_sub = max(max_sub, ed - idx_of_last_time_curr_prod_was_neg)


        '''

        max_len = 0
        last_idx = float('inf')

        curr_st, curr_prod = 0, 1
        for ed in range(len(nums)):
            if nums[ed] == 0:
                curr_prod = 1
                curr_st = ed + 1
                last_idx = float('inf')
                continue
            else:
                curr_prod *= nums[ed]

            if curr_prod > 0:
                max_len = max(max_len, ed - curr_st + 1)
            elif curr_prod < 0:
                max_len = max(max_len, ed - last_idx)
                if last_idx == float('inf'):
                    last_idx = ed

        return max_len
