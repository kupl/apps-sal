A,B,N= list(map(int,input().split()))

import math

if B-1 < N:
    print(math.floor(A*(B-1)/B) - A*math.floor((B-1)/B) )
else:
    print(math.floor(A*N/B) - A*math.floor(N/B))
