class Solution:
     def candy(self, ratings):
         """
         :type ratings: List[int]
         :rtype: int
         """
         if not ratings: return 0
         if len(ratings) == 1: return 1
         l2r = [1 for _ in ratings]
         for i in range(1, len(ratings)):
             if ratings[i] > ratings[i - 1]:
                 l2r[i] = l2r[i - 1] + 1
         res = l2r[-1]
         for i in range(len(ratings) - 2, -1, -1):
             if ratings[i] > ratings[i + 1]:
                 l2r[i] = max(l2r[i], l2r[i + 1] + 1)
             res += l2r[i]
         return res
