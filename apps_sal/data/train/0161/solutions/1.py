class Solution:
     def isValidSerialization(self, preorder):
         """
         :type preorder: str
         :rtype: bool
         """
         if not preorder:
             return False
         
         nodes = preorder.split(',')
         stack = [0] if nodes[0] != '#' else []
         dt = {0:2}
         i = 1
         
         while stack and i < len(nodes):
             dt[stack[-1]] -= 1
             if dt[stack[-1]] == 0:
                 stack.pop()
             if nodes[i] != '#':
                 stack.append(i)
                 dt[i] = 2
             i = i + 1
         
         return not stack and i == len(nodes)
         
         

