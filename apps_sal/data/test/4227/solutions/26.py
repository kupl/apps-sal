import itertools
N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(M)]
es = [[0] * N for _ in range(N)]
for a, b in AB:
    a, b = a - 1, b - 1
    es[a][b] = es[b][a] = 1

ans = 0
for ptn in itertools.permutations(range(1, N)):
    ptn = list(ptn)
    for a, b in zip([0] + ptn, ptn):
        if not es[a][b]:
            break
    else:
        ans += 1
print(ans)
