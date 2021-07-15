class Solution:
     def replaceWords(self, dt, sentence):
         """
         :type dict: List[str]
         :type sentence: str
         :rtype: str
         """
         trie = {}
         for w in dt:
             t = trie
             for c in w:
                 if c not in t:  t[c] = {}
                 t = t[c]
             t['#'] = w
             
         # result = []
         
 #         for word in sentence.split():
 #             result.append(self.replace(word, trie))
         
 #         return " ".joinresult 
     
 #     OR
         return  " ".join([ self.replace(i, trie) for i in sentence.split() ])
     
         
         
     
     def replace( self, word, trie ):
         cur = trie
         for letter in word:
             if letter not in cur: break
             cur = cur[letter]
             if "#" in cur:
                 return cur['#']
         return word
         
         
         setenceAsList = sentence.split(" ")
         for i in range(len(setenceAsList)):
             for j in dt:
                 if setenceAsList[i].startswith(j):
                     setenceAsList[i] = j
         return " ".join(setenceAsList)
     
         arrs = sentence.split()
         for i in range(len(arrs)):
             w = arrs[i]
             for j in range(len(arrs[i])):
                 cur = w[:j]
                 if cur in dt:
                     arrs[i] = cur
                     break
         return ' '.join(arrs)

