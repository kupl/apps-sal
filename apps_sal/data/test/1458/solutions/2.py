from sys import *
from math import *


N = int(input())

S = input()

f = -1

for i in range(1, N):
    if S[i] < S[i-1]:
        f = i
        break
    
if f == -1:
    print("NO")

else:
    print("YES")
    print(i, end=' ')
    print(i  + 1)
