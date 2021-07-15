class Solution:
     def leastBricks(self, wall):
         """
         :type wall: List[List[int]]
         :rtype: int
         """
         # use a hash to store edge location => number of bricks whose edge is on it
         # then the result is total_height - edge that has max of bricks
         if not wall: return 0
         hsh = collections.defaultdict(int)
         for row in wall:
             distance_from_left = 0
             # Notice you cannot go to the last one because the last edge will all be the width of the wall
             for brick_width in row[:-1]:
                 distance_from_left += brick_width
                 hsh[distance_from_left] += 1
         # notice hsh might be empty
         return len(wall) - max(list(hsh.values())+[0])
                 
 
         

