import itertools

N, C = map(int, input().split())
D = [0] + [[0] + list(map(int, input().split())) for i in range(C)]
c = [list(map(int, input().split())) for i in range(N)]

grid = [[], [], []]
for i in range(N):
    for j in range(N):
        grid[(i + j) % 3].append(c[i][j])

s = [[0] * (C + 1) for i in range(3)]

for i in range(3):
    for j in range(1, C + 1, 1):
        for k in range(len(grid[i])):
            s[i][j] += D[grid[i][k]][j]

ans = float("inf")
for p in itertools.permutations(list(range(1, C + 1)), 3):
    tmp = 0
    for i in range(3):
        tmp += s[i][p[i]]
    ans = min(tmp, ans)

print(ans)
