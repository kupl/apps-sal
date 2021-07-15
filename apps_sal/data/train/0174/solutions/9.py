class Solution:
     def lengthLongestPath(self, x):
         """
         :type input: str
         :rtype: int
         The number of tabs is my depth and for each depth I store the current path length.
 
 def lengthLongestPath(self, input):
     maxlen = 0
     pathlen = {0: 0}
     for line in input.splitlines():
         name = line.lstrip('\t')
         depth = len(line) - len(name)
         if '.' in name:
             maxlen = max(maxlen, pathlen[depth] + len(name))
         else:
             pathlen[depth + 1] = pathlen[depth] + len(name) + 1
     return maxlen        
         """
         h = {0:0}
         maxlen = 0
         #print(x.splitlines())
         for line in x.splitlines():
             name = line.lstrip('\t')
             depth = len(line)-len(name)
             if name.count('.') != 0:
                 maxlen = max(maxlen,h[depth]+len(name))
             else:
                 h[depth +1] = h[depth] + len(name) + 1
         return maxlen
