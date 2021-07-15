class Solution:   
     def wordBreak(self, s, wordDict):
         """
         :type s: str
         :type wordDict: List[str]
         :rtype: bool
         """
         canSplitUntilIndex = [False for x in range(len(s)+1)]
         canSplitUntilIndex[0] = True
         endIndex = 1
         while endIndex <= len(s):
             startIndex = 0
             splitIndex = startIndex
             while splitIndex < endIndex:
                 if canSplitUntilIndex[splitIndex] and s[splitIndex:endIndex] in wordDict:
                     canSplitUntilIndex[endIndex] = True
                     break
                 splitIndex += 1
             endIndex += 1
         
         return canSplitUntilIndex[len(s)]
             

