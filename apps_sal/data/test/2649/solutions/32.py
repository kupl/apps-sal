N=int(input())
A=[0]*(N)
B=[0]*(N)
for i in range(N):
    x,y=map(int, input().split())
    A[i]=x+y
    B[i]=x-y

A=sorted(A)
B=sorted(B)

print(max(A[-1]-A[0],B[-1]-A[0],A[-1]-A[0],B[-1]-B[0]))
