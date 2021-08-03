n, m = map(int, input().split())

bar = [{i} for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    bar[u].add(v)
    bar[v].add(u)

nodes = set(range(n))
ans = []

while (nodes):
    u = next(iter(nodes))
    nodes.remove(u)
    stk = [u]
    cnt = 1
    while (stk):
        v = stk.pop()
        s = nodes - bar[v]
        cnt += len(s)
        stk.extend(s)
        nodes &= bar[v]
    ans.append(cnt)

ans.sort()
print(len(ans))
print(' '.join(map(str, ans)))
