import sys
from itertools import accumulate
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = list(map(int, input().split()))
    A = list(map(int, input().split()))

    ans = list(accumulate(A))[-1]

    B = [0 for _ in range(52)]
    for i in reversed(list(range(51))):
        cnt1 = 0
        for j in range(n):
            if A[j] & (1 << i):
                cnt1 += 1

        cnt0 = n - cnt1
        if cnt0 > cnt1:
            B[i] = (1 << i) * (cnt0 - cnt1)

    pre = 0
    maxV = 0

    for i in reversed(list(range(51))):
        if k & (1 << i):
            total = 0
            for j in range(i):
                total += B[j]
            total += pre
            maxV = max(maxV, total)
            pre += B[i]

    maxV = max(maxV, pre)
    print((ans + maxV))


def __starting_point():
    resolve()

__starting_point()
