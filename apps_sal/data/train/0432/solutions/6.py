from heapq import *
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
      if len(nums) % k != 0:
        return False
      minHeap = []
      countsMap = {}
      for num in nums:
        if num not in countsMap:
          countsMap[num] = 1
          heappush(minHeap, num)
        else:
          countsMap[num] += 1
      
      while len(minHeap) > 0:
        minNum = heappop(minHeap)
        while countsMap[minNum] > 0:
          for i in range(k):
            currNum = minNum + i
            if currNum not in countsMap or countsMap[currNum] == 0:
              return False
            else:
              countsMap[currNum] -= 1
      
      return True
              

