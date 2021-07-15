import sys
sys.setrecursionlimit(2000000000)
N = int(input())
import math
l = [int(x) for x in input().split()]
tobi = [0]*(math.ceil(N/2))
tobi[0] = l[0]
for i in range(1,math.ceil(N/2)):
    tobi[i] = tobi[i-1] + l[i*2]
from functools import lru_cache
@lru_cache(maxsize=1000000000)
def motomeru(x,y):
    if y == 0 or x == 0 or x == 1:
        return 0
    elif x % 2 == 0:
        return max(motomeru(x-2,y-1)+l[x-1],tobi[math.floor((x-1)/2)])
    else:
        return max(motomeru(x-2,y-1)+l[x-1],motomeru(x-1,y))
print(motomeru(N,N//2))
