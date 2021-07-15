
import sys
import math
  
n = sys.stdin.readline()
m = sys.stdin.readline()

kn = [0] * 26
km = [0] * 26
for i in n:
    if(i != "\n"):
        kn[ord(i) - ord('a')] += 1
 
for i in m:
    if(i != "\n"):
        km[ord(i) - ord('a')] += 1      
        
res = 0
for i in range(26):
    v = min(kn[i], km[i])
    if(kn[i] == 0 and km[i] > 0):
        print(-1)
        return
    
    res += v    
  
print(res)  

