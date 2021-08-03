

"""k = []
for i in range(5):
    k.append([int(x) for x in (sys.stdin.readline()).split()])
    
vmax = 0 
tt = []
for i in range(5):
    for j in range(i, 5):
        if(i != j):
            k[i][j] = k[j][i] = k[i][j] + k[j][i]
                

for i in range(5):
    print(k[i])"""


import sys
import math

n = int(sys.stdin.readline())

k = [0] * 9

for i in range(4):
    tt = sys.stdin.readline()
    for j in range(4):
        if(tt[j] != '.'):
            ind = ord(tt[j]) - ord('0') - 1
            k[ind] += 1
            if(k[ind] > n * 2):
                print("NO")
                return

print("YES")
