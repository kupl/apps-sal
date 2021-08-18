

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


N = int(input())
L = [int(x) for x in input().split()]

res = 0
for i in range(0, N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            tempo = [L[i], L[j], L[k]]
            tempo.sort()

            if(tempo[0] + tempo[1] > tempo[2] and tempo[0] < tempo[1] and tempo[1] < tempo[2]):
                res += 1
print(res)
