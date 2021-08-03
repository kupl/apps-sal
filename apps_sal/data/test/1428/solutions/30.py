from collections import defaultdict

N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
grid = [list(map(int, input().split())) for _ in range(N)]

mod_0 = defaultdict(int)
mod_1 = defaultdict(int)
mod_2 = defaultdict(int)

for i in range(N):
    for j in range(N):
        n = (i + j + 2) % 3
        if n == 0:
            mod_0[grid[i][j]] += 1
        elif n == 1:
            mod_1[grid[i][j]] += 1
        else:
            mod_2[grid[i][j]] += 1

ans = float("inf")
for i in range(C):
    for j in range(C):
        if i == j:
            continue
        for k in range(C):
            if k in [i, j]:
                continue

            total = 0
            for prev, cnt in mod_0.items():
                total += D[prev - 1][i] * cnt
            for prev, cnt in mod_1.items():
                total += D[prev - 1][j] * cnt
            for prev, cnt in mod_2.items():
                total += D[prev - 1][k] * cnt

            ans = min(ans, total)
print(ans)
