import sys
import math
import itertools


def input():
    return sys.stdin.readline().rstrip()


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
                arr.append(i)
    if temp != 1:
        arr.append(temp)
    if arr == []:
        arr.append(n)
    return arr


def main():
    N = int(input())
    P = [0] * (N + 1)
    for i in range(1, N + 1):
        arr = factorization(i)
        for s in arr:
            P[s] += 1
    ans = 0
    PN = []
    for j in P:
        if j != 0:
            PN.append(j)
    ans = 0
    count = 0
    for i in PN:
        if i >= 74:
            count += 1
    ans += count
    count = 0
    sub1 = 0
    sub2 = 0
    for i in PN:
        if i >= 24:
            sub1 += 1
        if i >= 2:
            sub2 += 1
    ans += sub1 * (sub2 - 1)
    sub1 = 0
    sub2 = 0
    for i in PN:
        if i >= 14:
            sub1 += 1
        if i >= 4:
            sub2 += 1
    ans += sub1 * (sub2 - 1)
    sub1 = 0
    sub2 = 0
    for i in PN:
        if i >= 4:
            sub1 += 1
        if i >= 2:
            sub2 += 1
    ans += sub1 * (sub1 - 1) * (sub2 - 2) // 2
    print(ans)


def __starting_point():
    main()


__starting_point()
