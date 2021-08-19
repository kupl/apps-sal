import sys
sys.setrecursionlimit(10 ** 6)


def II():
    return int(sys.stdin.readline())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LC():
    return list(input())


def IC():
    return [int(c) for c in input()]


def MI():
    return map(int, input().split())


def solve():
    N = II()
    T = input()
    if N == 1:
        if T == '0':
            print(10000000000)
            return
        elif T == '1':
            print(20000000000)
            return
    elif N == 2:
        if T == '11' or T == '10':
            print(10000000000)
            return
        elif T == '01':
            print(9999999999)
            return
        else:
            print(0)
            return
    else:
        First = T[:3]
        if First != '110' and First != '101' and (First != '011'):
            print(0)
            return
        for i in range(3, N - 2, 3):
            if First != T[i:i + 3]:
                print(0)
                return
        if N % 3 == 1:
            if First[0] != T[-1]:
                print(0)
                return
        elif N % 3 == 2:
            if First[0:2] != T[-2:]:
                print(0)
                return
        from math import ceil, floor
        if First == '110':
            print(10000000000 - floor((N - 1) / 3))
            return
        elif First == '101' or First == '011':
            print(9999999999 - floor((N - 2) / 3))
            return
    return


solve()
