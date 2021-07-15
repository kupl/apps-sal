class Solution:
     
     def replaceWords(self, roots, sentence):
         
         # create a trie with roots words
 
         trie = {}
         for w in roots:
             t = trie
             for c in w:
                 if c not in t:  t[c] = {}
                 t = t[c]
             t['#'] = True
         # print(trie)
 #        result = []
         return  " ".join([ self.replace(i, trie) for i in sentence.split() ])
     
         
         
     
     def replace( self, word, trie ):
         cur = trie
         i=0
         for letter in word:
             if letter not in cur: break
             cur = cur[letter]
             i+=1
             if "#" in cur:
                 return word[:i]
         return word

