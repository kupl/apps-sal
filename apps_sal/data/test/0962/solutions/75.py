from collections import deque
n, m = list(map(int, input().split()))
path = [set() for _ in range(n)]
pathr = [set() for _ in range(n)]
for _ in range(m):
    a, b = list(map(int, input().split()))
    path[a - 1].add(b - 1)
    pathr[b - 1].add(a - 1)


def bfs(start):
    que = deque()
    d = [1e100] * n
    for i in path[start]:
        que.append(i)
        d[i] = 1
    while que:
        p = que.popleft()
        for nxt in path[p]:
            if d[nxt] == 1e100:
                que.append(nxt)
            d[nxt] = min(d[nxt], d[p] + 1)
    if d[start] == 1e100:
        return [0] * (n + 1)
    ret = [0] * d[start]
    ret[-1] = start
    now = start
    for i in range(d[start] - 1)[::-1]:
        for p in pathr[now]:
            if d[p] == i + 1:
                now = p
                ret[i] = now
                break
    return ret


ans = [0] * (n + 1)
for i in range(n):
    tmp = bfs(i)
    if len(ans) > len(tmp):
        ans = tmp
if len(ans) > n:
    print((-1))
else:
    print((len(ans)))
    for i in ans:
        print((i + 1))
