from collections import deque
N = int(input())
A = list(map(int, input().split()))
deq = deque()
for i in range(N):
    if i % 2 == 0:
        deq.appendleft(A[i])
    else:
        deq.append(A[i])
if N % 2 == 0:
    for i in reversed(range(N)):
        print(deq[i], end=" ")
else:
    for i in range(N):
        print(deq[i], end=" ")
