N, M = list(map(int, input().split()))

nE = [{i} for i in range(N)]
for _ in range(M):
    u, v = list(map(int, input().split()))
    u, v = u - 1, v - 1
    nE[u].add(v)
    nE[v].add(u)

unvisited = set(range(N))
res = []

while unvisited:
    s = next(iter(unvisited))
    unvisited.discard(s)
    stack = [s]
    cnt = 1
    while stack:
        v = stack.pop()
        s = unvisited - nE[v]
        cnt += len(s)
        stack.extend(s)
        unvisited &= nE[v]

    res.append(cnt)

res.sort()
print(len(res))
print(' '.join(map(str, res)))
