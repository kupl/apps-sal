from collections import deque
n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
A = deque(A)
B.sort()
for _ in range(n + 1):
    d = (A[0] - B[0]) % m
    for i in range(1, n):
        if (A[i] - B[i]) % m != d:
            d = -1
            break
    if d != -1:
        print(-d % m)
        return
    x = A.pop()
    A.appendleft(x)
print(-1)
