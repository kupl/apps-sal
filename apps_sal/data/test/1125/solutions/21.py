N=int(input())
A=list(map(int,input().split()))
X=0
if N>2:
    X=A[2]
for i in range(3,N):
    X=(X|A[i])-(X&A[i])
S=A[0]+A[1]
if (S-X)%2==1 or (S-X)<0:
    print(-1)
else:
    D=(S-X)//2
    if D&X>0:
        print(-1)
    else:
        a=D
        for i in range(50,-1,-1):
            if ((X>>i)&1) and ((a+(1<<i))<A[0]):
                a+=(1<<i)
        if a>0 and A[0]>=a:
            print(A[0]-a)
        else:
            print(-1)
