class Solution:
     def findContentChildren(self, g, s):
         """
         :type g: List[int]
         :type s: List[int]
         :rtype: int
         """
         g.sort()
         s.sort()
         print(g)
         print(s)
         
         count_child = 0
         count_cookie = 0
         
         while(count_child < len(g) and count_cookie < len(s)):
             if (g[count_child] <= s[count_cookie]):
                 count_child += 1
             count_cookie += 1
             
         return count_child
     

