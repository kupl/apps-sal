class Solution:
     def decodeString(self, s):
         """
         :type s: str
         :rtype: str
         """
         stack = []
         stack.append(["", 1])
         num = ""
         for ch in s:
             if ch.isdigit():
                 num += ch
             elif ch == '[':
                 stack.append(["", int(num)])
                 num = ""
             elif ch == ']':
                 st, k = stack.pop()
                 stack[-1][0] += st*k
             else:
                 stack[-1][0] += ch
         return stack[0][0]
 
         
         
         
         
         
         
         
         
         
         
         
 
 
 
 # def decodeString(self, s):
 #     while '[' in s:
 #         s = re.sub(r'(\d+)\[([a-z]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
 #     return s            

