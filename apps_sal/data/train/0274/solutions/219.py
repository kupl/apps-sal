import heapq
class Solution:
    def __init__(self):
        self.nums = None
        self.start = None
        self.end = None
        self.q = []
        self.qmx = []

        
    def initialize (self):
        self.start = 0
        self.end=0
        heapq.heappush(self.q,[self.nums[0],0])  
        heapq.heappush(self.qmx,[self.nums[0]*-1,0]) 
        
    def moveStartRight(self):
        #[2,5,3,1]  3
        # 1,2,3,5
        # 5,3,2,1
        count = 0
        # get min and max
        #move to the right until the min or max are popped up 
        minValuePos = self.q[0][1]
        maxValuePos = self.qmx[0][1]
        self.start = min (minValuePos,maxValuePos) +1
        
        #update new q
        while self.q[0][1] < self.start:
            heapq.heappop(self.q)
        while self.qmx[0][1] < self.start:
            heapq.heappop(self.qmx)
        
        
        #self.q = []
        #for i in range(self.start, self.end +1):
        #    self.q.append([self.nums[i],i])
        #heapq.heapify(self.q)
        
        
    def moveEndRight(self):
        self.end +=1
        if self.end < len(self.nums):
            heapq.heappush(self.q,[self.nums[self.end], self.end]) 
            heapq.heappush(self.qmx,[self.nums[self.end]*-1, self.end]) 
        
    def getMinMax(self):
        return self.q[0][0], self.qmx[0][0]*-1
        
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        self.nums = nums
        self.initialize()
        size = 0
        while (self.end < len(self.nums)):
            minValue,maxValue = self.getMinMax()
            #print(self.start, self.end, minValue,maxValue)
            if maxValue - minValue <= limit:
                #print(minValue, maxValue, nums[start:end+1])
                size = max(size, self.end - self.start + 1)
                #extend 
                self.moveEndRight()
            else:
                self.moveStartRight()


        return size
        

