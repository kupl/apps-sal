
import sys
import math
  
st = sys.stdin.readline()
l = len(st) - 1

dct = {'A' : 1, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 1, 'I': 1,
        'J': 0, 'K': 0, 'L': 0, 'M': 1, 'N': 0, 'O': 1, 'P': 0, 'Q': 0, 'R': 0, 'S': 0,
        'T': 1, 'U': 1, 'V': 1, 'W': 1, 'X': 1, 'Y': 1, 'Z': 0 }

if(l % 2 != 0):
    if(dct[st[int(l / 2)]] == 0):
        print("NO")
        return

j = l
for i in range(int(l / 2)):
    if(st[i] != st[j - 1] or dct[st[i]] == 0):
        print("NO")
        return
        
    j -= 1
        
print("YES")


