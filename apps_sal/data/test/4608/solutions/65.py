import sys
N = int(input())
A ={}
for i in range(1,N+1):
    A[i] = int(input())
#print(A)
ans = 1
x = 1
for j in range(N):
    if A[x] == 2:
        print(ans)
        return
    x = A[x]
    ans += 1
print(-1)
