class Solution:
     def simplifyPath(self, path):
         """
         :type path: str
         :rtype: str
         """
         if not path or len(path)==1:
             return path
         stack = []
         list_path = path.split('/')
         for ch in list_path:
             if ch == '..':
                 if stack: stack.pop()
             elif ch != '.' and ch:
                 stack.append(ch)
         return '/'+'/'.join(stack)
