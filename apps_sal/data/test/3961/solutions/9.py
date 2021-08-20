import sys


def solve():
    mod = 1000 * 1000 * 1000 + 7
    (n,) = rv()
    (a,) = rl(1)
    mem = [0] * n
    timesofar = 0
    for i in range(n):
        ariveat = a[i] - 1
        moresum = 0
        for j in range(ariveat, i):
            moresum += mem[j]
        mem[i] = moresum + 2
        timesofar += moresum + 2
        timesofar %= mod
    print(timesofar)


def rv():
    return list(map(int, input().split()))


def rl(n):
    return [list(map(int, input().split())) for _ in range(n)]


if sys.hexversion == 50594544:
    sys.stdin = open('test.txt')
solve()
