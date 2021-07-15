

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        low = None
        curr_max = None
        curr_low = -1
        max_len = 0
        min_queue = []
        max_queue = []
        for i in range (len(nums)):
            curr_num = nums[i]
            self.queue_add_max(max_queue,curr_num,i)
            self.queue_add_min(min_queue,curr_num,i)
            curr_max = max_queue[0][0]
            curr_min = min_queue[0][0]
            if (curr_max - curr_min) > limit:
                while ((curr_max - curr_min) > limit) and (curr_low < i):
                    curr_low += 1
                    if (curr_low == min_queue[0][1]):
                        min_queue.pop(0)
                    if (curr_low == max_queue[0][1]):
                        max_queue.pop(0)
                    curr_max = max_queue[0][0]
                    curr_min = min_queue[0][0]    
            curr_dist = i - curr_low
            if (curr_dist > max_len):
                max_len = curr_dist
        return max_len
                            
        
    def queue_add_max(self,queue,element,index):
        while (queue != []):
            if element > queue[len(queue) - 1][0]:
                queue.pop()
            else:
                break
        queue.append((element,index))

    def queue_add_min(self,queue,element,index):
        while (queue != []):
            if element < queue[len(queue) - 1][0]:
                queue.pop()
            else:
                break
        queue.append((element,index))
