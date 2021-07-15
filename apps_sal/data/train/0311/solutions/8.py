class Solution:
     def candy(self, ratings):
         """
         :type ratings: List[int]
         :rtype: int
         """
         candies = [0] * len(ratings)
         # min candies at idx i = max of
         # 1) (number of decreasing ratings to the left) + 1
         # 2) (number of decreasing ratings to the right) + 1
         # By definition number after end of decreasing sequence will be greater than the end
         # => both sides of end of decreasing sequence will be greater than the rating at the end
         # => the min number of candies at the end of the decreasing sequence is 1
         # => min number of candies at the (end-n) of the decreasing sequence is 1+n        
         from_left = [1] * len(ratings)
         cur_less_than = 1
         for idx in range(1, len(ratings)):
             if ratings[idx-1] < ratings[idx]:
                 cur_less_than += 1
             else:
                 cur_less_than = 1
             from_left[idx] = cur_less_than
         
         from_right = [1] * len(ratings)
         cur_less_than = 1
         idx = len(ratings)-2
         while idx >= 0:
             if ratings[idx+1] < ratings[idx]:
                 cur_less_than += 1
             else:
                 cur_less_than = 1
             from_right[idx] = cur_less_than
             idx -= 1
             
         for idx in range(0, len(ratings)):
             candies[idx] = max(from_left[idx], from_right[idx])
             
         return sum(candies)
