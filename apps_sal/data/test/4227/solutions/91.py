from itertools import permutations

N, M = map(int, input().split())
edges = set(tuple(map(int, input().split())) for _ in range(M))

ans = 0
for t in permutations(range(2, N + 1)):
    p = [1] + list(t)
    ok = True
    for i in range(N - 1):
        e = tuple(sorted((p[i], p[i + 1])))
        if not (e in edges):
            ok = False
            break
    if ok:
        ans += 1

print(ans)
