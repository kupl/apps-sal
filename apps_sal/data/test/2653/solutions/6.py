from collections import deque
(N, Q) = map(int, input().split())
f = [[] for i in range(N)]
for i in range(N - 1):
    (a, b) = map(int, input().split())
    f[a - 1].append(b - 1)
    f[b - 1].append(a - 1)
ans = [0] * N
for i in range(Q):
    (p, x) = map(int, input().split())
    ans[p - 1] += x
d = deque()
d.append(0)
root = [-1] * N
root[0] = 0
while len(d) > 0:
    z = d.popleft()
    for i in f[z]:
        if root[i] == -1:
            root[i] = z
            ans[i] += ans[z]
            d.append(i)
print(*ans)
