N,M=list(map(int,input().split()))
L,R=list(map(int,input().split()))
for i in range(M-1):
    H,I=list(map(int,input().split()))
    if H>L:
        L=H
    if R>I:
        R=I
    if R<L:
        break
if R<L:
    print((0))
else:
    ans=list(range(L,R+1))
    print((len(ans)))

