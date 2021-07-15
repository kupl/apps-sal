class Solution:
     def wordBreak(self, s, wordDict):
         """
         :type s: str
         :type wordDict: List[str]
         :rtype: bool
         """
         word_set = set(wordDict)
         return self._dfs(s, 0, word_set, {})
     
     def _dfs(self, s, start, word_set, memoization):
         if start == len(s):
             return True
         
         if start in memoization:
             return memoization[start]
         
         for end in range(start, len(s) + 1):
             if s[start:end] in word_set and self._dfs(s, end, word_set, memoization):
                 memoization[start] = True
                 return True
         
         memoization[start] = False
         return False
