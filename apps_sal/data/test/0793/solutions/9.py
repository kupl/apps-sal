# coding: utf-8
import sys
input = sys.stdin.readline

MOD = int(1e9 + 7)


def f(N, M, s, t):
    cums = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(N):
        cumsi = cums[i]
        cumsi1 = cums[i + 1]
        for j in range(M):
            num = 0
            if s[i] == t[j]:
                num = cumsi[j] + 1
            cumsi1[j + 1] = \
                (cumsi1[j] + cumsi[j + 1] - cumsi[j] + num) % MOD
    return((cums[N][M] + 1) % MOD)


n, m = list(map(int, input().split()))
s = list(map(int, input().split()))
t = list(map(int, input().split()))
print((f(n, m, s, t)))
