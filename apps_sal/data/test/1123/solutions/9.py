import copy
import random
import bisect
import fractions
import math
import sys
import collections
mod = 10 ** 9 + 7
sys.setrecursionlimit(mod)
d = collections.deque()


def LI():
    return list(map(int, sys.stdin.readline().split()))


(N, K) = LI()
'\nX = gcd(A_1, A_2,...A_K)\nとなるようなXを考えると溶ける\nX = 3の時その個数は\n[K/3]**N\n'
x_cnt = [0] * (K + 1)
for x in range(K, 0, -1):
    tmp = pow(K // x, N, mod)
    for j in range(x + x, K + 1, x):
        tmp -= x_cnt[j]
    x_cnt[x] = tmp
ans = 0
for i in range(1, K + 1):
    ans += i * x_cnt[i]
    ans %= mod
print(ans)
