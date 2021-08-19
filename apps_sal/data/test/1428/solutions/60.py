from itertools import permutations
(N, C) = list(map(int, input().split()))
D = [list(map(int, input().split())) for i in range(C)]
colors = [[0] * C for i in range(3)]
for i in range(N):
    tmp = list(map(int, input().split()))
    for (j, color) in enumerate(tmp):
        num = (i + 1 + (j + 1)) % 3
        colors[num][color - 1] += 1
data = [[0] * C for i in range(3)]
for i in range(3):
    for j in range(C):
        for k in range(C):
            data[i][k] += colors[i][j] * D[j][k]
ans = 10 ** 10
for iter_ in permutations(list(range(C)), 3):
    tmp = []
    for (i, j) in enumerate(iter_):
        tmp.append(data[i][j])
    ans = min(ans, sum(tmp))
print(ans)
