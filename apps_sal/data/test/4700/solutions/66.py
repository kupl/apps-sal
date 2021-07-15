N,M = map(int,input().split())
H = [int(i) for i in input().split()]
A = []
B = []
for i in range(M):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
I = []
ans = 0
for i in range(1,N+1):
    I.append([i])
for i in range(M):
    I[A[i]-1].append(B[i])
    I[B[i]-1].append(A[i])
for i in range(N):
    count = 0
    a = H[i]
    if(count < 2):
        for j in range(len(I[i])):
            if(H[I[i][j]-1] >= a):
                count += 1
    if(count < 2):
        ans += 1
print(ans)
