N=int(input())
A=list(map(int,input().split()))
S=A[0]+A[1]
X=0
for i in range(2,N):
    X=X^A[i]
if (S-X)%2==1 or S<X:
    print((-1))
    return
D=(S-X)//2
if X&D!=0:
    print((-1))
    return
a=0
#print(X,D)
B=[0 for i in range(42)]
for k in range(41,-1,-1):
    x=(X&(1<<k))>>k
    d=(D&(1<<k))>>k
    if (x,d)==(0,0):
        pass
    elif (x,d)==(0,1):
        a=a^(1<<k)
    elif (x,d)==(1,0):
        B[k]=1
    else:
        pass
for k in range(41,-1,-1):
    if B[k]==0:
        continue
    if a^(1<<k)<A[0]:
        a=a^(1<<k)
if 0<a<=A[0]:
    print((A[0]-a))
else:
    print((-1))

