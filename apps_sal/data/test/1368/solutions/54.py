import sys
from collections import Counter
from itertools import product
from random import randint

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def debug(n, a, b, V, ave):
    cnt = 0
    for pattern in product([0, 1], repeat=n):
        if a <= sum(pattern) <= b:
            tot = 0
            for idx, p in enumerate(pattern):
                if p == 1:
                    tot += V[idx]
            res = tot / sum(pattern)
            if abs(res - ave) <= 10 ** -6:
                cnt += 1
    return cnt


def resolve():
    n, a, b = list(map(int, input().split()))
    V = list(map(int, input().split()))

    V.sort(reverse=True)
    ave = 0
    for i in range(a, b + 1):
        tot = sum(V[:i])
        if ave <= tot / i:
            ave = tot / i
            used = V[:i]

    if len(set(used)) == 1:
        cnt = V.count(used[0])
        ave = used[0]
        cmb = [0] * len(used)
        for i in range(a, len(used) + 1):
            x = y = 1
            for j in range(1, i + 1):
                x *= (cnt + 1 - j)
                y *= j
            cmb[i - 1] = x // y
        res = sum(cmb)
    else:
        use_cnt = Counter(used)
        used = set(used)
        D = Counter(V)
        res = 1
        for num in used:
            cnt = use_cnt[num]
            x = y = 1
            for j in range(1, cnt + 1):
                x *= (D[num] + 1 - j)
                y *= j
            res *= x // y
    print(ave)
    print(res)


def __starting_point():
    resolve()


__starting_point()
