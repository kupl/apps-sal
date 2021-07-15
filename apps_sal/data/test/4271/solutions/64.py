N=int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
S = 0

for i in range(N):
    S += B[A[i]-1]


for i in range(N-1):
    if A[i]-A[i+1] == -1:
        S += C[A[i]-1]
print(S)

