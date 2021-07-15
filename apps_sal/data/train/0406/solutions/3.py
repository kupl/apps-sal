class Solution:
     def ladderLength(self, beginWord, endWord, wordList):
         """
         :type beginWord: str
         :type endWord: str
         :type wordList: List[str]
         :rtype: int
         """
         letters ='abcdefghijklmnopqrstuvwxyz'
         wordList = set(wordList)
         if endWord not in wordList:
             return 0
         reached = set()
         backreached = set()
         reached.add(beginWord)
         backreached.add(endWord)
         wordList.discard(beginWord)
         wordList.discard(endWord)
         depth = 1
         while not (reached & backreached):
             toAdd = set()
             for word in reached:
                 for i,letter in enumerate(word):
                     for newletter in letters:
                         if newletter != letter:
                             newword = word[:i] + newletter + word[i+1:]
                             if newword in backreached:
                                 return depth + 1
                             elif newword in wordList:
                                 toAdd.add(newword)
                                 wordList.remove(newword)
             if len(toAdd) == 0:
                 return 0
             else:
                 depth += 1
                 reached = toAdd
                 if len(reached) > len(backreached):
                     reached, backreached = backreached, reached
         return depth
