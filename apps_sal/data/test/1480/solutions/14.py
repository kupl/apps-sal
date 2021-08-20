from collections import deque
(N, K) = list(map(int, input().split()))
A = list(map(int, input().split()))
q = deque(list(range(1, N + 1)))
ret = []
for k in range(K):
    for a in range(A[k] % len(q)):
        q.append(q.popleft())
    ret.append(q.popleft())
print(' '.join([str(r) for r in ret]))
