from itertools import permutations

N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
c = [list(map(int, input().split())) for _ in range(N)]

# グリッド座標を3種類に分ける
rem = [[] for _ in range(3)]
for i in range(N):
    for j in range(N):
        rem[(i + j + 2) % 3].append(c[i][j])
# print(rem)

cost = [[] for _ in range(3)]

for i in range(3):
    for s in range(C):
        tmp = 0
        for t in rem[i]:
            tmp += D[t - 1][s]
        cost[i].append((tmp, s + 1))

for i in cost:
    i.sort()
    i = i[:3]

ans = 1e10
for i in cost[0]:
    for j in cost[1]:
        for h in cost[2]:
            if i[1] != j[1] and j[1] != h[1] and h[1] != i[1]:
                ans = min(ans, i[0] + j[0] + h[0])
print(ans)
