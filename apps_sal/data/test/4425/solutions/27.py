#ABC126 C

import math
N,K = map(int,input().split())
P = 0
for i in range(1,N+1):
    if i >= K:
        P += 1/N
    else:
        P += (1/N)*(0.5)**(math.ceil(math.log(K/i,2)))
        
print(P)
