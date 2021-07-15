N,K=list(map(int,input().split()))
h=[0]*N
for H in range(N):
    h[H-1]=int(input())
A=sorted(h)
L=K-1
M=A[L]-A[0]
O=(N-K)+1
for j in range(O):
    if M>A[L+j]-A[j]:
        M=A[L+j]-A[j]
print(M)

