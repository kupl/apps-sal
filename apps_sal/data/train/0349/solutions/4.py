class Solution:
     def deleteAndEarn(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         from collections import Counter
         c = Counter(nums)
         n = len(nums)
         pick = {-math.inf:0}
         miss = {-math.inf:0}
         prev = -math.inf
         for (num, freq) in sorted(c.items()):
             if prev == num - 1:
                 pick[num] = miss[num-1] + num*freq
                 miss[num] = max(miss[num-1], pick[num-1])
             else:
                 pick[num] = max(miss[prev], pick[prev]) + num*freq
                 miss[num] = max(miss[prev], pick[prev])
             prev = num
             # print(num, pick, miss)
         return max(pick[prev], miss[prev])
