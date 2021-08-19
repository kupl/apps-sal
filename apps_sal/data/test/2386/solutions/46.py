import math
N = int(input())
A = list(map(int, input().split()))
for i in range(1, N + 1):
    A[i - 1] -= i
A.sort()
if N % 2 == 0:
    mid = N // 2 - 1
    ans = 0
    for i in range(N):
        ans += abs(A[i] - A[mid])
    tmp = 0
    for i in range(N):
        tmp += abs(A[i] - A[mid + 1])
    ans = min(ans, tmp)
    print(ans)
else:
    mid = N // 2
    ans = 0
    for i in range(N):
        ans += abs(A[i] - A[mid])
    print(ans)
