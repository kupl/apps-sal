N=int(input())
A=list(map(int, input().split()))
B=[0]*N
C=''
 
for i in range(N):
    B[A[i]-1]=i+1
 
for i in range(N):
    C+=str(B[i])+' '
 
print(C[0:-1])
