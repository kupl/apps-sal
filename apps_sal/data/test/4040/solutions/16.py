import sys


n, m, d = list(map(int, input().split()))
M = list(map(int, sys.stdin.readline().split())) 
sumM = sum(M)
A = [0] * n
posit = -1
for platf in range(m):
    for ii in range(posit + min(d, n - sumM - posit), posit + min(d, n - sumM - posit) + M[platf]):
        A[ii] = platf + 1
    posit = ii
    sumM -= M[platf]    
if n - posit > d:
    print("NO")
else:
    print("YES")
    print(*A)

