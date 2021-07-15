import itertools


def calc(colo, target, d_mtx):
    ret = 0
    for i, item in enumerate(colo):
        ret += item * d_mtx[i][target]
    return ret


n, c = list(map(int, input().split()))
d_mtx = []
c_mtx = []

for i in range(c):
    d_mtx.append(list(map(int, input().split())))

for i in range(n):
    c_mtx.append(list(map(int, input().split())))

color = [[0] * c for _ in range(3)]

for i in range(n):
    for j in range(n):
        color[((i+1)+(j+1)) % 3][c_mtx[i][j]-1] += 1

ret = 10 ** 10
for item in itertools.permutations(list(range(c)), 3):
    tmp = 0
    for i in range(3):
        tmp += calc(color[i], item[i], d_mtx)
    ret = min(ret, tmp)

print(ret)

