class Solution:
     def threeSumClosest(self, array, target):
         """ Returns sum of integers from array closest to target.
         Time complexity: O(n ^ 2). Space complexity: O(n),
         where n is len(array).
         """
         array.sort()
 
         n = len(array)
         best_sum = float("inf")  # closest sum of 3 integers so far
         for i in range(n - 2):  # choosing the 1st integer
             if i > 0 and array[i] == array[i - 1]:  # skip duplicates
                 continue
 
             diff = target - array[i]  # best sum for 2 other integers
             x, y = i + 1, n - 1
             best_diff = float("inf")
             while x < y:
                 curr_diff = array[x] + array[y]
                 if curr_diff == diff:  # exact sum we're looking for
                     return target
                 elif curr_diff < diff:  # increase current sum of 2 integers
                     x += 1
                 else:  # curr_diff > diff, decrease current sum of 2 integers
                     y -= 1
                 # update best difference so far
                 if abs(curr_diff - diff) < abs(best_diff - diff):
                     best_diff = curr_diff
 
             # update best sum if needed
             curr_sum = array[i] + best_diff
             if abs(curr_sum - target) < abs(best_sum - target):
                 best_sum = curr_sum
         return best_sum
