class Solution:
  def minOperations(self, nums: List[int]) -> int:
    maxDivideCount = 0
    minusCount = 0
    for num in nums:
      divideCount = 0
      while num != 0:
        if num % 2 == 0:
          num //= 2
          divideCount += 1
        else:
          num -= 1
          minusCount += 1
      maxDivideCount = max(divideCount, maxDivideCount)
    return maxDivideCount + minusCount
    
#     while self.isAllZero(nums) is False:
#       if self.isAllEven(nums):
#         nums = [a // 2 for a in nums]
#         count += 1
#         continue
#       for i in range(len(nums) - 1):
#         if nums[i] != 0 and nums[i] % 2 == 1:
#           nums[i] -= 1
#           count += 1
        
#     return count
      
#   def isAllZero(self, nums: List[int]) -> bool:
#     for n in nums:
#       if n != 0:
#         return False
#     return True
  
#   def isAllEven(self, nums: List[int]) -> bool:
#     for n in nums:
#       if n % 2 != 0:
#         return False
#     return True
    

