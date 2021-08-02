# ABC150D

from math import gcd, ceil
import sys
input = sys.stdin.readline


def main():
    N, M = list(map(int, input().split()))
    A = list([int(x) // 2 for x in input().split()])
    lcm = A[0]
    for i in range(1, N):
        lcm = lcm * A[i] // gcd(lcm, A[i])
    allo = 1
    for i in range(N):
        allo &= (lcm // A[i]) % 2
    if allo:
        print((ceil(int(M // lcm) / 2)))
    else:
        print((0))


def __starting_point():
    main()


__starting_point()
