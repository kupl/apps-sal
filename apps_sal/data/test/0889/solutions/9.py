import sys
import math

t = []

for i in range(4):
    t.append([x for x in sys.stdin.readline() if x != '\n'])
    
for i in range(1, 4):

    for j in range(1, 4):
        c = 0
        if(t[i][j] != t[i - 1][j]):
            c += 1
        if(t[i][j] != t[i - 1][j - 1]):
            c += 1
        if(t[i][j] != t[i][j - 1]):
            c += 1     
        if(c != 2):
            print("YES")
            return
        
print("NO")
        

