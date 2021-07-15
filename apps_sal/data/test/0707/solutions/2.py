from sys import *
from math import *
from collections import *

N, M = map(int, input().split())

events = list(map(int, input().split()))

p = list(map(int, input().split()))

g = events[1] - events[0]

for i in range(2, N):
    g = gcd(g, events[i] - events[i-1])
    
f = None

for i in range(M):
    if g % p[i] == 0:
        
        f =i + 1
        break

if f == None:
    print("NO")

else:
    print("YES")
    print(events[0],end=' ')
    print(f)    

