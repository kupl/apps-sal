N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
s=0
for i in range(N):
    s+=B[A[i]-1]
    if A[i]-A[i-1]==1 and i>0:
        s+=C[A[i]-2]
print(s)
