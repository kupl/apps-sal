class Solution:    
    def lastSubstring(self, s: str) -> str:
        charInd = collections.defaultdict(list)
        # head = {}
        for i in range(len(s)):
            charInd[s[i]].append(i)        
        maxChr = max(charInd.keys())
        
        if len(charInd[maxChr]) == len(s)-1:
            return s
        
        m = s[-1]
        for i in charInd[maxChr]:
            m = max(m, s[i:])
        return m
            
            
            
            # node = head
#             for c in s[i:]:
#                 if c not in node:
#                     node[c] = {}
#                 node = node[c]
            
#         res = \"\"
#         node = head
#         while node:
#             ch = max(node.keys())
#             res += ch
#             node = node[ch]           
        
#         return res

