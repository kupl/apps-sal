from collections import defaultdict
import itertools
n, c = list(map(int, input().split()))
D = [list(map(int, input().split()))for _ in range(c)]


# 色は0始まりで管理する

# 入力の色を受け取って、それぞれの色毎にいくつあるか
diago0 = defaultdict(int)
diago1 = defaultdict(int)
diago2 = defaultdict(int)

for i in range(n):
    for j, color in enumerate(map(int, input().split())):
        color -= 1
        if (i + j) % 3 == 0:
            diago0[color] += 1
        elif (i + j) % 3 == 1:
            diago1[color] += 1
        else:
            diago2[color] += 1


# 0列目をcにするときのcにするときの最小コスト
cost0 = [0] * c
cost1 = [0] * c
cost2 = [0] * c

for i in range(c):
    for k, v in list(diago0.items()):
        cost0[i] += D[k][i] * v
for i in range(c):
    for k, v in list(diago1.items()):
        cost1[i] += D[k][i] * v
for i in range(c):
    for k, v in list(diago2.items()):
        cost2[i] += D[k][i] * v

INF = 10**18
ans = INF
for trio in itertools.combinations(list(range(c)), 3):
    for a, b, c in itertools.permutations(trio, 3):
        cost = cost0[a] + cost1[b] + cost2[c]
        if cost < ans:
            ans = cost
print(ans)
