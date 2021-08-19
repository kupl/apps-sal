from collections import deque
(n, b) = map(int, input().split())
q = deque()
for i in range(n):
    (t, d) = map(int, input().split())
    while len(q) > 0 and q[0] <= t:
        q.popleft()
    if len(q) <= b:
        r = t if len(q) == 0 else q[-1]
        print(r + d, end=' ')
        q.append(r + d)
    else:
        print(-1, end=' ')
