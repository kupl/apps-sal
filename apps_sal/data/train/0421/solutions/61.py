class Solution:
    def lastSubstring(self, s: str) -> str:
        # Algorithm
        # First look for the max letter starting points
        i, j, k = 0, 1, 0
        N = len(s)      
        
        while j + k < N:
            if s[i+k] == s[j+k]:
                k += 1
                continue
            elif s[i+k] > s[j+k]:
                j = j+k+1
            else:
                i = i+k+1
                j = i+1
            k = 0
        return s[i:]
#         max_letter = None
#         indexes = []
#         for i, c in enumerate(s):
#             if max_letter is None or c > max_letter:
#                 max_letter = c
#                 indexes = [(i, i+1)]
#             elif max_letter == c:
#                 indexes.append((i, i+1))
                
#         # Now we iterate over them like a queue
#         while len(indexes) != 1:
#             new_indexes = []
#             new_max_letter = None
            
#             for tup in indexes:
#                 if tup[1] >= len(s):
#                     continue
                          
#                 if new_max_letter is None or s[tup[1]] > new_max_letter:
#                     new_indexes = [(tup[0], tup[1] + 1)]
#                     new_max_letter = s[tup[1]]
#                 elif s[tup[1]] == new_max_letter:
#                     new_indexes.append((tup[0], tup[1] + 1))
#             indexes = new_indexes
        
#         return s[indexes[0][0]:]

