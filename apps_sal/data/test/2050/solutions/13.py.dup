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

# 12 14 16 20
# 2 * 2 * 3   2 * 7   2 * 2 * 2 * 2   2 * 3 * 3
# 1 2 3 5
# 7 8 9 11
# 13
# 19
# 25
# 31


def prt(l): return print(' '.join(l))
def rv(): return map(int, input().split())
def rl(n): return [list(map(int, input().split())) for _ in range(n)]


if sys.hexversion == 50594544:
    sys.stdin = open("test.txt")
solve()
