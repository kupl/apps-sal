class Solution(object):
     def removeKdigits(self, num, k):
         """
         :type num: str
         :type k: int
         :rtype: str
         """
         if k == len(num):
             return "0"
         stack = []
         cnt = 0
         for i, ch in enumerate(num):
             if cnt == k:
                 for j in range(i, len(num)):
                     stack.append(num[j])
                 break
             if not stack or ch >= stack[-1]:
                 stack.append(ch)
             else:
                 while stack and ch < stack[-1] and cnt < k:
                     stack.pop()
                     cnt += 1
                 stack.append(ch)
         while cnt < k:
             stack.pop()
             cnt += 1
         i = 0
         while i < len(stack) and stack[i] == '0':
             i += 1
         if i == len(stack):
             return "0"
         return ''.join(stack[i:])
