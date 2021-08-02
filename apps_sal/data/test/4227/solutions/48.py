import itertools
N, M = map(int, input().split())

g = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

p = list(itertools.permutations(range(0, N)))

ans = 0
for pair in p:
    if pair[0] != 0:
        continue
    ok = True
    for node1, node2 in zip(pair[0:], pair[1:]):
        if node1 not in g[node2]:
            ok = False
            break
    if ok:
        ans += 1

print(ans)
