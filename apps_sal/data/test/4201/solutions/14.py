

import math
import copy
import string

INF = int(10**18)
pi = math.pi

MOD = 1000000007


def my_pow(N, a, M):
    if(a == 0):
        return 1
    else:
        if(a % 2 == 0):
            tempo = my_pow(N, a / 2, M)
            return (tempo * tempo) % M
        else:
            tempo = my_pow(N, a - 1, M)
            return (tempo * N) % M


def my_combination(N, a, M):
    res = 1

    for i in range(0, a):
        res *= N - i
        res %= M

    for i in range(0, a):
        res *= my_pow(i + 1, M - 2, M)
        res %= M

    return res


def my_combination_table(N, M, v):
    if(len(v) < N + 1):
        l = N + 1 - len(v)
        tempo = [1] * l
        v.extend(tempo)

    for i in range(1, N + 1):
        v[i] = v[i - 1] * (N - (i - 1))
        v[i] %= M

        v[i] *= my_pow(i, M - 2, M)
        v[i] %= M

    return


H, W, K = (int(x) for x in input().split())
c = [input() for i in range(0, H)]

res = 0
for i in range(0, 2 ** H):
    for j in range(0, 2 ** W):
        cnt = 0
        for h in range(0, H):
            for w in range(0, W):
                if(c[h][w] == '
                    cnt += 1
        if(cnt == K):
            res += 1

print(res)
