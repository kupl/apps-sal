class Solution:
     def ladderLength(self, beginWord, endWord, wordList):
         """
         :type beginWord: str
         :type endWord: str
         :type wordList: List[str]
         :rtype: int
         """
         wordList=set(wordList)
         if endWord not in wordList:
             return 0
         beginSet=set()
         endSet=set()
         visited=set()
         res=1
         beginSet.add(beginWord)
         endSet.add(endWord)
         while len(beginSet)!=0 and len(endSet)!=0:
             if len(beginSet)>len(endSet):
                 beginSet,endSet=endSet,beginSet
             tmp=set()
             for word in beginSet:
                 chs=list(word)
                 for i in range(len(chs)):
                     for ch in range(ord('a'),ord('z')+1):
                         old=chs[i]
                         chs[i]=chr(ch)
                         target="".join(chs)
                         if target in endSet:
                             return res+1
                         if target not in visited and target in wordList:
                             tmp.add(target)
                             visited.add(target)
                         chs[i]=old
             beginSet=tmp
             res+=1
         return 0

