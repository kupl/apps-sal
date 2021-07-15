from itertools import permutations


N, M, *ab = list(map(int, open(0).read().split()))
g = [[] for _ in range(N)]
for a, b in zip(*[iter(ab)] * 2):
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

ans = 0
for path in permutations(list(range(1, N))):
    v = 0
    for nv in path:
        if nv not in g[v]:
            break
        v = nv
    else:
        ans += 1
print(ans)


