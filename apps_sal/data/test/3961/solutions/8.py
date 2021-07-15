import sys

def solve():
    mod = 1000 * 1000 * 1000 + 7
    n, = rv()
    a, = rl(1)
    a.append(0)
    mem = [0] * (n + 1)
    timesofar = 0
    for i in range(n + 1):
        ariveat = a[i] - 1
        moresum = 0
        for j in range(ariveat, i):
            moresum += mem[j]
        mem[i] = moresum + 1
        timesofar += moresum + 1
        timesofar %= mod
    print(timesofar - 1)


def rv(): return list(map(int, input().split()))
def rl(n): return [list(map(int, input().split())) for _ in range(n)]
if sys.hexversion == 50594544 : sys.stdin = open("test.txt")
solve()



