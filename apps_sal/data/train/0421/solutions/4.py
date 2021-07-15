class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j, offset = 0, 1, 0
        while i + offset < len(s) and j + offset < len(s):
            if s[i + offset] == s[j + offset]:
                offset += 1
            else:
                if s[i + offset] < s[j + offset]:
                    i += offset + 1
                else:
                    j += offset + 1
                if i == j:
                    j += 1
                offset = 0
        return s[i :]
        
        
        
#         maxchar = 'a'
#         index = []
        
#         for i in range(len(s)):
#             if s[i] > maxchar:
#                 maxchar = s[i]
#                 index.append(i)
#         # print(index)
#         maxstring = \"\"
        
#         for i in range(len(index)):
#             if s[index[i]:] > maxstring:
#                 maxstring = s[index[i]:]
                
#         return maxstring
        
        
        
        
#         m = \"\" 
#         for i in range(len(s)): 
#             m = max(m, s[i:]) 
  
#         return m



