from collections import deque
n = int(input())
A = list(map(int, input().split()))
b = deque()
for i in range(1, n + 1):
    if i % 2 == 1:
        b.append(A[i - 1])
    else:
        b.appendleft(A[i - 1])
if n % 2 == 1:
    for i in range(n - 1, -1, -1):
        print(b[i], end='')
        if i != 0:
            print(' ', end='')
else:
    for i in range(n):
        print(b[i], end='')
        if i != n - 1:
            print(' ', end='')
