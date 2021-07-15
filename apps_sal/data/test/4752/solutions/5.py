# Using 'dict', like hash, to find the pair number
 class Solution:
     def twoSum(self, numbers, target):
         ans = []
         dir = {}
         ll = len(numbers)
         for i in range(ll):
             dir[numbers[i]] = i
         for i in range(ll):
             o2 = target-numbers[i]
             if o2 in dir:
                 if (dir[o2] != i):
                     ans.append(i)
                     ans.append(dir[o2])
                     return ans
