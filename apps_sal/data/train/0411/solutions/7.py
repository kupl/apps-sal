class Solution:
     def wordBreak(self, s, wordDict):
         """
         :type s: str
         :type wordDict: List[str]
         :rtype: bool
         """
         l = set(wordDict)
         stack = [-1]
         for i in range(len(s)):
             ptr = len(stack) - 1
             while ptr >= 0:
                 if s[stack[ptr] + 1:i + 1] in l:
                     stack.append(i)
                     break
                 ptr -= 1
         return stack[-1] == len(s) - 1
