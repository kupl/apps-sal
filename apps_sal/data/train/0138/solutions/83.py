class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def getMaxLenHelper(nums: List[int]) -> int:
           ans = 0
           count,count1,negativeCount = 0,0,0
           for i in range(len(nums)):
              if nums[i] == 0:
                  if count > ans:
                     ans = count
                  count,count1,negativeCount = 0,0,0
              else:
                if nums[i] > 0:
                    count += 1
                count1 += 1
                if nums[i] < 0:
                   negativeCount += 1
                   if negativeCount == 2:
                      count = count1
                      negativeCount = 0
                   else:
                      if count > ans:
                         ans = count
                      count = 0
           if count > ans:
              ans = count
           return ans
        return max(getMaxLenHelper(nums),getMaxLenHelper(nums[::-1]))
        
            

