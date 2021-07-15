class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        global_max = 0
        curr_neg = 0
        curr_pos = 0
        neg_flag = False
        
        for num in nums:
            if num == 0:
                # global_max = max(global_max, local_max)
                local_max = 0
                curr_neg = 0
                curr_pos = 0
                neg_flag = False
            elif num > 0:
                curr_pos += 1
                curr_neg += 1
            else:
                curr_neg += 1
                curr_pos = 0
                neg_flag = not neg_flag
            if neg_flag == False:
                global_max = max(global_max, curr_neg)
            else:
                global_max = max(global_max, curr_pos)
        
        curr_neg = 0
        curr_pos = 0
        neg_flag = False
        for num in nums[::-1]:
            if num == 0:
                # global_max = max(global_max, local_max)
                local_max = 0
                curr_neg = 0
                curr_pos = 0
                neg_flag = False
            elif num > 0:
                curr_pos += 1
                curr_neg += 1
            else:
                curr_neg += 1
                curr_pos = 0
                neg_flag = not neg_flag
            if neg_flag == False:
                global_max = max(global_max, curr_neg)
            else:
                global_max = max(global_max, curr_pos)
        
        return global_max
