N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

res = - 10 ** 18
for i in range(1, 2 ** 10):
    tmp = [0] * N
    for j in range(10):
        if i >> j & 1:
            for k in range(N):
                tmp[k] += F[k][j]
    res_tmp = 0
    for j in range(N):
        res_tmp += P[j][tmp[j]]
    res = max(res, res_tmp)

print(res)

