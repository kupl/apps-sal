class Solution:
     def lengthLongestPath(self, input):
         """
         :type input: str
         :rtype: int
         """
         maxlen = 0
         path = {0:0}
         for line in input.splitlines():
             name = line.lstrip('\t')
             depth = len(line) - len(name)
             if '.' in line:
                 maxlen = max(maxlen, path[depth] + len(name))
             else:
                 path[depth + 1] = path[depth] + len(name) + 1
         return maxlen
                 
         
              
         
             
                 
                 
                 
             
             

