N = int(input())
A = list(map(int,input().split()))
cmax = 0
a = 0
ind = -1
for i in range(N):
    if abs(A[i])>cmax:
        cmax = abs(A[i])
        a = A[i]
        ind = i
if a>0:
    B = []
    for i in range(N):
        if A[i]<0:
            A[i] += a
            B.append([ind+1,i+1])
    for i in range(1,N):
        A[i] += A[i-1]
        B.append([i,i+1])
    print(len(B))
    for j in range(len(B)):
        print(*B[j])
elif a<0:
    B = []
    for i in range(N):
        if A[i]>0:
            A[i] += a
            B.append([ind+1,i+1])
    for i in range(N-2,-1,-1):
        A[i] += A[i+1]
        B.append([i+2,i+1])
    print(len(B))
    for j in range(len(B)):
        print(*B[j])
else:
    print(0)
