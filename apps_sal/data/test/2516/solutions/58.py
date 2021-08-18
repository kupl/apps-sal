import sys
import numpy as np

input = sys.stdin.readline


def ST():
    return input().rstrip()


def I():
    return int(input())


def MI():
    return list(map(int, input().split()))


def LI():
    return list(MI())


N, P = MI()
S = ST()

ans = 0
if P == 2:
    for i, s in enumerate(S, 1):
        if int(s) % 2 == 0:
            ans += i
elif P == 5:
    for i, s in enumerate(S, 1):
        if int(s) % 5 == 0:
            ans += i
else:
    cnt = np.zeros(P)
    cnt[0] = 1
    res = 0
    tmp = 1
    for s in S[::-1]:
        res += int(s) * tmp
        res %= P
        cnt[res] += 1
        tmp *= 10
        tmp %= P

    for c in cnt[cnt >= 2]:
        ans += c * (c - 1) // 2

print((int(ans)))
