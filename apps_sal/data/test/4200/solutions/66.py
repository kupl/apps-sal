(n, m) = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
A.reverse()
s = 0
cnt = 0
for i in range(n):
    s += A[i]
for i in range(m):
    if A[i] >= s / (4 * m):
        cnt += 1
if cnt == m:
    print('Yes')
else:
    print('No')
