from collections import deque

n, m = map(int, input().split())

ans = [-1 for _ in range(n + 1)]
ans[0] = 0
ans[1] = 0

V = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    V[x].append(y)
    V[y].append(x)

d = deque([1])

while d:
    l = d.popleft()
    for v in V[l]:
        if ans[v] != -1:
            continue
        ans[v] = l
        d.append(v)


if ans.count(-1) > 0:
    print('No')
else:
    print('Yes')
    print(*ans[2:], sep="\n")
