N = int(input())
import math
for _ in range(N):
    x,y,p,q = [int(x) for x in input().split()]
    if (p == 0) or (p==q):
        if (x*q == p*y):
            print(0)
        else:
            print(-1)
        continue
    n = math.ceil((y-x)/(q-p))
    n = max(n,math.ceil(x/p))
    n = max(n,math.ceil(y/q))
    print(n*q-y)

