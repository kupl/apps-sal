import numpy as np

N,K=map(int,input().split())
p=list(map(lambda x:(int(x)+1)/2,input().split()))

if N==K:
    print(sum(p))
else:
    cs=np.cumsum(p)
    m=[]
    for i in range(N-K):
        m.append(cs[K+i]-cs[i])

    print(max(m))
