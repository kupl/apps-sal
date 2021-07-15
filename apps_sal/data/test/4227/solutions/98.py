from itertools import permutations

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)

res = 0
for P in permutations(range(N), N):
    if P[0] != 0:
        continue
    for i in range(N - 1):
        if P[i + 1] not in G[P[i]]:
            break
    else:
        res += 1

print(res)
