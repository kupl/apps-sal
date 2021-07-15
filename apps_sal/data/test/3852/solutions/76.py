N = int(input())
A = list(map(int,input().split()))
amin = min(A)
indmin = A.index(amin)+1
amax = max(A)
indmax = A.index(amax)+1
if amin>=0:
    print((N-1))
    for i in range(1,N):
        print((i,i+1))
elif amax<=0:
    print((N-1))
    for i in range(N,1,-1):
        print((i,i-1))
elif amax+amin>=0:
    print((2*(N-1)))
    for i in range(1,N+1):
        if i!=indmax:
            print((indmax,i))
    for i in range(1,N):
        print((i,i+1))
elif amax+amin<0:
    print((2*(N-1)))
    for i in range(1,N+1):
        if i!=indmin:
            print((indmin,i))
    for i in range(N,1,-1):
        print((i,i-1))

