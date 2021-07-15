class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        
        
        mymap = collections.defaultdict(int)
        st, j, n = 0, 0, len(s)
#         charmap = collections.defaultdict(int)
        
#         for i in range(st, st+minSize-1):
#             charmap[s[i]] += 1
#         # print(charmap)
        while st + minSize <= n:
            # print (st)
            count = collections.Counter(s[st:st+minSize-1])
            for j in range(st+minSize-1, st+maxSize):
                
                if j >= n:
                    break
                    
                count[s[j]] += 1
                if len(count) <= maxLetters:
                    mymap[s[st:j+1]] += 1
                
                
                
                
                
#                 print(j, s[st:])
#                 if j >= n:
#                     break
                    
#                 charmap[s[j]] += 1
#                 if len(charmap) <= maxLetters:
#                     mymap[s[st:j+1]] += 1
                
                 
#             charmap[s[st]] -= 1
#             if charmap[s[st]] <= 0:
#                 charmap.pop(s[st])
            st += 1
                    
        # ans = 0  
        maxval = max(list(mymap.values()) or [0])
        # for key in mymap:
        #     if mymap[key] == maxval:
        #         ans += 1
                
        return maxval
        # print(mymap)
        
        
        
        
        
        
        
        
        

