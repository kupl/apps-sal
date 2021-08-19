import sys
import math


def count(a, b, N):
    keta = len(str(N))
    cnt = 0
    if a == b:
        cnt += 1 if a <= N else 0
    if keta == 1:
        return cnt
    if keta == 2:
        cnt += 1 if b * 10 + a <= N else 0
        return cnt
    for k in range(2, keta):
        cnt += 10 ** (k - 2)
    s = N // 10 ** (keta - 1)
    t = N % 10
    if b > s:
        return cnt
    elif b < s:
        cnt += 10 ** (keta - 2)
    else:
        tempN = (N - s * 10 ** (keta - 1) - t) // 10
        cnt += tempN + 1
        if a > t:
            cnt -= 1
    return cnt


def count_aa(a, N):
    keta = len(str(N))
    cnt = 0
    if keta == 1:
        return 1 if a <= N[-1] else 0
    cnt += 1
    if keta == 2:
        return cnt + 1 if a <= N[-1] else 0
    for k in range(2, keta):
        cnt += 10 ** (k - 2)
    s = N // 10 ** (keta - 1)
    t = N % 10
    if b > s:
        return cnt
    elif b < s:
        cnt += 10 ** (keta - 2)
    else:
        tempN = (N - s * 10 ** (keta - 1) - t) // 10
        cnt += tempN + 1
        if a > t:
            cnt -= 1
    return cnt


N = int(input())
c = 0
for i in range(1, N + 1):
    a = int(str(i)[0])
    b = i % 10
    if b == 0:
        continue
    c += count(a, b, N)
print(c)
