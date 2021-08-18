import sys


def solve():
    n, k, = rv()
    res = list()
    cur = 1
    for i in range(n):
        while cur % 2 == 0:
            cur += 1
        res.append(((cur) * k, (cur + 1) * k, (cur + 2) * k, (cur + 4) * k))
        cur += 5
    print(res[-1][-1])
    print('\n'.join((' '.join(map(str, l))) for l in res))


def prt(l): return print(' '.join(l))
def rv(): return map(int, input().split())
def rl(n): return [list(map(int, input().split())) for _ in range(n)]


if sys.hexversion == 50594544:
    sys.stdin = open("test.txt")
solve()
