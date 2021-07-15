class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        hmin, hmax = [], []
        heapq.heapify(hmin), heapq.heapify(hmax)
        max_length = 0
        i,j = 0, 0
        heapq.heappush(hmin, (nums[0],0)), heapq.heappush(hmax, (-1*nums[0],0))
        while j<len(nums):
            while hmax[0][1]<i: heapq.heappop(hmax)
            while hmin[0][1]<i: heapq.heappop(hmin)
            if -1*(hmax[0][0]+hmin[0][0])<=limit: 
                max_length = max(max_length, j-i+1)
                j+=1
                if j>=len(nums): break
                heapq.heappush(hmin, (nums[j], j))
                heapq.heappush(hmax, (-1*nums[j], j))
            else:
                i+=1
        return max_length
