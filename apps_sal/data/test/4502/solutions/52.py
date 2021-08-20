from collections import deque
n = int(input())
A = list(map(int, input().split()))
deq = deque()
for i in range(n):
    if i % 2 == 0:
        deq.appendleft(A[i])
    else:
        deq.append(A[i])
if n % 2 == 0:
    for i in reversed(range(n)):
        print(deq[i], end=' ')
else:
    for i in range(n):
        print(deq[i], end=' ')
