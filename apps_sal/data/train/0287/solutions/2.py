class Solution:
     def __init__(self):
         self._cache = {}
 
     def countArrangement(self, N):
         """Now given N, how many beautiful arrangements can you construct?
 
         Suppose you have N integers from 1 to N. We define a beautiful
         arrangement as an array that is constructed by these N numbers
         successfully if one of the following is true for the ith position (1 <=
         i <= N) in this array:
 
             The number at the ith position is divisible by i.
             i is divisible by the number at the ith position.
 
         Args:
             N, int.
 
         Returns:
             count, int.
         """
         return self.countHelper(N, tuple(range(1, N + 1)))
 
     def countHelper(self, i, array):
         if i == 1:
             return 1
         key = (i, array)
         if key in self._cache:
             return self._cache[key]
         total = 0
         for j in range(len(array)):
             if array[j] % i == 0 or i % array[j] == 0:
                 total += self.countHelper(i - 1, array[:j] + array[j + 1:])
         self._cache[key] = total
         return total
