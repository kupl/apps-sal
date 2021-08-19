(a, b) = map(int, input().split())
P = list(map(int, input().split()))
flag = 0
M = P[0]
m = P[0]
for i in range(a):
    M = max(M, P[i])
    m = min(m, P[i])
s = max(M, 2 * m)
A = list(map(int, input().split()))
for i in range(b):
    if A[i] <= s:
        flag = 1
if flag == 1:
    print(-1)
else:
    print(s)
