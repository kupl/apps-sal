import math
from collections import Counter
from itertools import combinations
from collections import defaultdict


def factorization(n):
    arr = {}
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr[i] = cnt
    if temp != 1:
        arr[temp] = 1
    if len(list(arr.keys())) == 0:
        arr[n] = 1
    return arr


def prepare(n, MOD):
    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
    return (factorials, invs)


MOD = 1000000007


def solve():
    (N, M) = list(map(int, input().split()))
    temp = factorization(M)
    max_num = max(temp.values())
    (factorials, invs) = prepare(N + max_num - 1, MOD)
    ans = 1
    for (i, j) in list(temp.items()):
        if i == 1:
            break
        ans *= factorials[N + j - 1]
        ans %= MOD
        ans *= invs[N - 1]
        ans %= MOD
        ans *= invs[j]
        ans %= MOD
    print(ans)


def __starting_point():
    solve()


__starting_point()
