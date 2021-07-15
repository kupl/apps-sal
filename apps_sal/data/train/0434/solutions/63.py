class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0 
        r = 0
        earliest_one = float('inf')
        earliest_zero = float('inf')
        zeros = 1
        max_len = 0
        while(r < len(nums)):
            zeros -= nums[r] == 0
            if(zeros < 0):
                zeros += nums[l] == 0
                l += 1
            r += 1
        return r - l - 1
        
        '''#queue kind of slow
        l = 0
        r = 0
        max_len = 0
        zeros = 0
        queue = []
        while(r < len(nums)):
            if(nums[r] == 0 and zeros < 1):
                zeros = 1
                queue.append(nums[r])
                max_len = max(max_len, len(queue))
                r += 1
            elif(nums[r] == 0 and zeros == 1):
                if(queue[0] == 0):
                    #zero in front
                    while(len(queue) > 0 and queue[0] == 0):
                        queue.pop(0)
                #zero in the middle
                else:
                    while(len(queue) > 0 and queue[0] == 1):
                        queue.pop(0)
                    queue.pop(0)
                queue.append(nums[r])
                max_len = max(max_len, len(queue))
                r += 1
            elif(nums[r] == 1):
                queue.append(nums[r])
                max_len = max(max_len, len(queue))
                r += 1
        return max_len-1'''
