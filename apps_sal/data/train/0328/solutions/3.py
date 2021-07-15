class Solution:
     def find132pattern(self, nums):
         """
         :type nums: List[int]
         :rtype: bool
         """
         if len(nums) < 3: return False
         
         low = [float('inf')]
         high = [float('inf')]
         currlow, currhigh = nums[0], nums[0]
         for i in range(1, len(nums)):
             # print(nums[i])
             while nums[i] > high[-1]:
                 low.pop()
                 high.pop()
             if low[-1] < nums[i] < high[-1]:
                 return True
             if nums[i] == currlow or nums[i] == currhigh:
                 continue
             elif nums[i] < currlow:
                 low.append(currlow)
                 high.append(currhigh)
                 currlow, currhigh = nums[i], nums[i]
             elif nums[i] > currhigh:
                 currhigh = nums[i]
             else:
                 return True
             # print(currlow, currhigh)
             # print(low)
             # print(high)
         
         return False

