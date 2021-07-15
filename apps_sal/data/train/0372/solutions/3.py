class Solution:
     def __init__(self):
         self.dp = {}
 
     def isMatch(self, text, pattern):
         if not pattern:
             return not text
         
         if (text, pattern) in self.dp:
             return self.dp[(text, pattern)]
 
         first_match = bool(text) and pattern[0] in {text[0], '.'}
 
         if len(pattern) >= 2 and pattern[1] == '*':
             
             self.dp[(text, pattern)] = self.isMatch(text, pattern[2:]) or \
                                        first_match and self.isMatch(text[1:], pattern)
         else:
             self.dp[(text, pattern)] = first_match and self.isMatch(text[1:], pattern[1:])
         
         return self.dp[(text, pattern)]
