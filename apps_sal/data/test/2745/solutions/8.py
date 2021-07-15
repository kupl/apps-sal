class Solution:
     def findSubstring(self, s, words):
         """
         :type s: str
         :type words: List[str]
         :rtype: List[int]
         """
         L = len(s)
         length = len(words[0])
         Length = length * len(words)
         result = []
         word_dict = {}
         for word in words:
             word_dict[word] = word_dict[word]+1 if word in word_dict else 1
         for i in range(length):
             l = i
             r = i
             curr_dict={}
             while r+length<=L:
                 word  = s[r:r+length]
                 r = r+length
                 if word in word_dict:
                     curr_dict[word] = curr_dict[word]+1 if word in curr_dict else 1
                     while curr_dict[word] > word_dict[word]:
                         curr_dict[s[l:l+length]] -=1
                         l += length
                     if r-l==Length:
                         result.append(l)
                 else:
                     curr_dict.clear()
                     l = r
             
         return result
 

