# -*- coding: utf-8 -*-
import sys
from collections import deque


input = sys.stdin.readline


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input().strip()


def read_str_n():
    return list(map(str, input().split()))


def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        error_print(e - s, 'sec')
        return ret

    return wrap


@mt
def slv(N, R, X):
    X.sort()
    X = deque(X)
    l = 0
    r = N-1
    ll = 0
    while X:
        r = X.pop()
        while X:
            rr = X.pop()
            if rr != r:
                X.append(rr)
                break
        ll += R

        while X:
            l = X.popleft()
            if l > ll:
                X.appendleft(l)
                break

    return ll // R


def main():
    Q = read_int()

    for _ in range(Q):
        N, R = read_int_n()
        X = read_int_n()
        print(slv(N, R, X))


def __starting_point():
    main()

__starting_point()
