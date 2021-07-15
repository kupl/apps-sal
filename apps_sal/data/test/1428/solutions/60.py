#!/usr/bin/env python3

from itertools import permutations

N, C = list(map(int, input().split()))

D = [list(map(int, input().split())) for i in range(C)]
# c = [list(map(int, input().split())) for i in range(N)]

colors = [[0]*C for i in range(3)]
for i in range(N):
    tmp = list(map(int, input().split()))
    for j, color in enumerate(tmp):
        num = ((i+1) + (j+1)) % 3
        colors[num][color-1] += 1
# print(colors)

data = [[0]*C for i in range(3)]


for i in range(3):
    # color[i]
    for j in range(C):
        for k in range(C):
            data[i][k] += colors[i][j] * D[j][k]
# print(data)

ans = 10**10
for iter_ in permutations(list(range(C)), 3):
    # print(iter_)
    tmp = []
    for i, j in enumerate(iter_):
        tmp.append(data[i][j])
    ans = min(ans, sum(tmp))
print(ans)

