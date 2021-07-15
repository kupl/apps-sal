N=int(input())
A=list(map(int,input().split()))
A.sort(reverse=True)
if N%2==0:
    x=A[0]
    x+=sum(A[1:N//2])*2
    print(x)
else:
    x=A[0]
    x+=sum(A[1:(N-1)//2])*2
    x+=A[(N-1)//2]
    print(x)

