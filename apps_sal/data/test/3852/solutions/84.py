N = int(input())
A = list(map(int,input().split()))
amax = max(A)
amin = min(A)
if amax+amin>=0:
    imax = A.index(amax)
    imax += 1
    m = 2*N-2
    print(m)
    for i in range(1,N+1):
        if i != imax:
            print(imax,i)
    for i in range(1,N):
        print(i,i+1)
else:
    imin = A.index(amin)
    imin += 1
    m = 2*N-2
    print(m)
    for i in range(1,N+1):
        if i!=imin:
            print(imin,i)
    for i in range(N,1,-1):
        print(i,i-1)
