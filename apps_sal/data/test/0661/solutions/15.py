from itertools import chain
m,k=map(int,input().split())
if 0<k<2**m and m>=2:
    print(*[str(i) for i in chain(range(0,k),range(k+1,2**m),[k],range(2**m-1,k,-1),range(k-1,-1,-1),[k])])
elif k==0:
    print(*[str(i) for i in chain(range(0,2**m),range(2**m-1,-1,-1))])
else:
    print(-1)
