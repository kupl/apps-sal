from collections import deque
import sys
input = sys.stdin.readline
(n, m) = list(map(int, input().split()))
back = [[] for i in range(n)]
for _ in range(m):
    (u, v, w) = list(map(int, input().split()))
    u -= 1
    v -= 1
    back[v].append((u, w))
out = [2] * n
outl = [-1] * n
outl[-1] = 0
q = deque([n - 1])
while q:
    v = q.popleft()
    for (u, w) in back[v]:
        if out[u] != w:
            out[u] = 1 - w
        elif outl[u] == -1:
            outl[u] = outl[v] + 1
            q.append(u)
out = [v if v != 2 else 1 for v in out]
print(outl[0])
print(''.join(map(str, out)))
