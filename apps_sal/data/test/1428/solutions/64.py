import itertools

N, C = map(int, input().split())
D = [list(map(int, input().split())) for i in range(C)]
c = [list(map(int, input().split())) for i in range(N)]

indices = [2, 0, 1]
count_color = [[0] * C for i in range(3)]
for i in range(N):
    idx = indices[i % 3]
    for j in range(N):
        count_color[idx][c[i][j] - 1] += 1
        idx = (idx + 1) % 3

ans = float('inf')
correspondence = list(itertools.permutations(range(C), 3))
for corr in correspondence:
    cost = 0
    for idx in range(3):
        for color in range(C):
            cost += count_color[idx][color] * D[color][corr[idx]]
    ans = min(ans, cost)

print(ans)
