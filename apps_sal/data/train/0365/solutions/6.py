# from collections import defaultdict
# class Solution(object):
#     def uniqueLetterString(self, s):
#         \"\"\"
#         :type S: str
#         :rtype: int
#         \"\"\"
#         dic = defaultdict(list)
#         for i,letter in enumerate(s):
#             dic[letter].append(i)
        
#         pos = {letter:0 for letter in dic.keys()}
#         res = 0
#         for i,letter in enumerate(s):
#             idx = pos[letter]
            
#             if idx - 1 >= 0:
#                 left = dic[letter][idx - 1] + 1
#             else:
#                 left = 0
#             if idx + 1 <= len(dic[letter]) - 1:
#                 right = dic[letter][idx + 1] - 1
#             else:
#                 right = len(s) - 1
            
#             res += (i - left + 1) * (right - i + 1)
#             pos[letter] += 1
        
#         return res % (10 ** 9 +7)
from collections import defaultdict
class Solution(object):
    def uniqueLetterString(self,S):
        # write your code in Python 3.6
        dictionary = dict()
    
        for i in range(len(S)):
            if dictionary.get(S[i]):
                dictionary[S[i]].append(i)
            else:
                dictionary[S[i]] = [i]
        position = dict()
        for letter in dictionary.keys():
            position[letter]=0
        result = 0
        for index, letter in enumerate(S):
            i = position[letter]
            if i-1>=0:
                l = dictionary[letter][i-1]+1
            else:
                l=0
            if i+1 <= len(dictionary[letter])-1:
                r = dictionary[letter][i+1]-1
            else:
                r = len(S) - 1

            result += ((index-l+1) * (r-index +1)) % 1000000007
            position[letter]+=1
        return result % 1000000007
