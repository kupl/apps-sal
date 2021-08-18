
import sys

n, m = list(map(int, input().split()))

ls = [[i] + list(map(int, input().split())) for i in range(m)]

ls.sort(key=lambda x: x[2])
d = dict(list(zip(list(range(1, n + 1)), [0 for i in range(n)])))


for i in range(m):
    ls[i].append(d[ls[i][1]] + 1)
    d[ls[i][1]] += 1
    ls[i].append(str(ls[i][1]).zfill(6) + str(ls[i][3]).zfill(6))

ls.sort(key=lambda x: x[0])

for l in ls:
    print((l[-1]))
