import math
import itertools

N, D = list(map(int, input().split()))
cnt = 0
L = []

for i in range(N):
    X = list(map(int, input().split()))
    L.append(X)

for i in itertools.combinations(L, 2):
    y, z, dis = i[0], i[1], 0
    for a, b in zip(y, z):
        dis += (a - b)**2
    if math.sqrt(dis) == int(math.sqrt(dis)):
        cnt += 1

print(cnt)
