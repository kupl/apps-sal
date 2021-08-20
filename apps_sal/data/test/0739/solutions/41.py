import sys
from collections import deque
import numpy as np
sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().rstrip()


def YesNo(b):
    return bool([print('Yes')] if b else print('No'))


def YESNO(b):
    return bool([print('YES')] if b else print('NO'))


def int1(x):
    return int(x) - 1


def main():
    (L, A, B, M) = map(int, input().split())

    def S(i):
        return A + B * i
    sec = []

    def nibutan(ok, ng, k):
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if solve(mid, k):
                ok = mid
            else:
                ng = mid
        return ok

    def solve(mid, k):
        return len(str(S(mid))) < k
    left = L - 1
    for k in range(19, 0, -1):
        if len(str(S(left))) == k:
            right = nibutan(-1, left, k)
            sec.append((k, left, right))
            left = right
    X = np.array([0, A % M, 1], dtype=np.int64)
    for (k, left, right) in sec[::-1]:
        n = left - right
        doubling = [np.array([[pow(10, k, M), 0, 0], [1, 1, 0], [0, B % M, 1]], dtype=np.int64)]
        for i in range((10 ** 18).bit_length()):
            doubling.append(np.dot(doubling[i], doubling[i]) % M)
        n = left - right
        for i in range(len(doubling)):
            if n & 1:
                X = np.dot(X, doubling[i]) % M
            n >>= 1
            if n == 0:
                break
    print(X[0])


def __starting_point():
    main()


__starting_point()
