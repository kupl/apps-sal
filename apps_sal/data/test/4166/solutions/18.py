import sys
import math
import decimal
import itertools
from itertools import product
from functools import reduce


def input():
    return sys.stdin.readline()[:-1]


def sort_zip(a: list, b: list):
    z = list(zip(a, b))
    z = sorted(z)
    (a, b) = list(zip(*z))
    a = list(a)
    b = list(b)
    return (a, b)


def main():
    (N, M) = list(map(int, input().split()))
    s = [0] * M
    c = [0] * M
    for i in range(M):
        (s[i], c[i]) = list(map(int, input().split()))
    if M == 0:
        if N == 1:
            print(0)
            return
        elif N == 2:
            print(10)
            return
        elif N == 3:
            print(100)
            return
    for i in range(M):
        if s[i] == 1 and c[i] == 0 and (N > 1):
            print(-1)
            return
    (s, c) = sort_zip(s, c)
    for i in range(M - 1):
        if s[i] == s[i + 1]:
            if c[i] != c[i + 1]:
                print(-1)
                return
    for i in range(1, N + 1):
        if i not in s:
            s.append(i)
            if i == 1:
                c.append(1)
            else:
                c.append(0)
    (s, c) = sort_zip(s, c)
    k = 1
    ans = ''
    for i in range(len(s)):
        if s[i] == k:
            ans += str(c[i])
            k += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
