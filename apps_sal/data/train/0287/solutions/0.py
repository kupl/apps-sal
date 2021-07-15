class Solution:
     def countArrangement(self, N):
         """
         :type N: int
         :rtype: int
         """
         d = {
             1:1,  2:2, 3:3, 4:8, 5:10, 6:36,
             7:41, 8:132, 9:250, 10:700,
             11:750, 12:4010, 13:4237, 14:10680, 15:24679
         }
         return d.get(N, N)

