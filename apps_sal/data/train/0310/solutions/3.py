class Solution:
     def monotoneIncreasingDigits(self, N):
         """
         :type N: int
         :rtype: int
         """
         NN = ('000000000000000000' + str(N))[-11:]
         chron = '0'
         for i in range(10):
             maxpossible = int(chron[-1])
             for fill in range(int(chron[-1]),10):
                 if chron + str(fill)*(10-i) <= NN:
                     maxpossible = fill
             chron = chron + str(maxpossible)
         return int(chron)
 

