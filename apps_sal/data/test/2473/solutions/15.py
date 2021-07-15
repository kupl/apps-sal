import itertools

N, K = map(int, input().split())
P = [tuple(map(int, input().split())) for _ in range(N)]

X = sorted([x for x, _ in P])
Y = sorted([y for _, y in P])
dict_x = {v: k + 1 for k, v in enumerate(X)}
dict_y = {v: k + 1 for k, v in enumerate(Y)}

table = [[0] * (N + 1) for _ in range(N + 1)]
for x, y in P:
    table[dict_y[y]][dict_x[x]] = 1

for x in range(N + 1):
    for y in range(N):
        table[y + 1][x] += table[y][x]
for y in range(N + 1):
    for x in range(N):
        table[y][x + 1] += table[y][x]

ans = float('inf')
for x1, x2 in itertools.combinations(range(N), 2):
    for y1, y2 in itertools.combinations(range(N), 2):
        if table[y2 + 1][x2 + 1] - table[y2 + 1][x1] - table[y1][x2 + 1] + table[y1][x1] >= K:
            ans = min(ans, (X[x2] - X[x1]) * (Y[y2] - Y[y1]))
print(ans)
