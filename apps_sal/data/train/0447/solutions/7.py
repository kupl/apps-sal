class Solution:
     def removeDuplicateLetters(self, s):
         """
         :type s: str
         :rtype: str
         """
         counts = {}
         for c in s:
             if c not in counts:
                 counts[c] = 0
             counts[c] += 1
 
         stack = []
         visited = set()
         for c in s:
             counts[c] -= 1
             if c in visited:
                 continue
             while stack and stack[-1] > c and counts[stack[-1]] > 0:
                 visited.remove(stack.pop())
 
             stack.append(c)
             visited.add(c)
 
         return ''.join(stack)

