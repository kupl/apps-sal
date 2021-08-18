from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A, reverse=True)


queue_A = deque(A)
queue_B = deque()

for i in range(M):
    if len(queue_B) > 0 and queue_B[0] >= queue_A[0]:
        queue_A.appendleft(queue_B.popleft())
    queue_A[0] //= 2
    if len(queue_A) > 1 and queue_A[0] < queue_A[1]:
        queue_B.append(queue_A.popleft())

print(sum(queue_A) + sum(queue_B))
