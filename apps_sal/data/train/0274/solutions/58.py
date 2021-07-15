class minMonotonicQueue(object):
    
    def __init__(self):
        self.queue = collections.deque([]) # non-descreasing
    
    def push(self, num, idx):
        while len(self.queue) != 0 and self.queue[-1][0] > num:
            self.queue.pop()
        self.queue.append((num, idx))
    
    def pop(self, idx):
        if self.queue[0][1] == idx:
            self.queue.popleft()
    
class maxMonotonicQueue(object):
    
    def __init__(self):
        self.queue = collections.deque([]) # non-increasing
    
    def push(self, num, idx):
        while len(self.queue) != 0 and self.queue[-1][0] < num:
            self.queue.pop()
        self.queue.append((num, idx))    
        
    def pop(self, idx):
        if self.queue[0][1] == idx:
            self.queue.popleft()

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ptr1, ptr2 = 0, 0
        res = 0
        minQ, maxQ = minMonotonicQueue(), maxMonotonicQueue()
        while ptr1 < len(nums) and ptr2 < len(nums):
            
            # push  
            minQ.push(nums[ptr2], ptr2)
            maxQ.push(nums[ptr2], ptr2)
            
            # print (ptr1, ptr2, minQ.queue, maxQ.queue)
            while maxQ.queue[0][0] - minQ.queue[0][0] > limit:
                ptr1 += 1
                
                if ptr1 > maxQ.queue[0][1]:
                    maxQ.pop(maxQ.queue[0][1])
                
                if ptr1 > minQ.queue[0][1]:
                    minQ.pop(minQ.queue[0][1])
            
                # print ('*', ptr1, ptr2, minQ.queue, maxQ.queue)
            res = max(res, ptr2 - ptr1 + 1)
            ptr2 += 1
        return res

