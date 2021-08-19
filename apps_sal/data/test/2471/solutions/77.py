from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)


def int1(x):
    return int(x) - 1


def p2D(x):
    return print(*x, sep='\n')


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def MI1():
    return map(int1, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def SI():
    return sys.stdin.readline()[:-1]


(h, w, n) = MI()
sq = defaultdict(int)
for _ in range(n):
    (a, b) = MI1()
    for i in range(max(0, a - 2), min(h - 2, a + 1)):
        for j in range(max(0, b - 2), min(w - 2, b + 1)):
            sq[i, j] += 1
cnt = [0] * 10
for (k, v) in sq.items():
    cnt[v] += 1
cnt[0] = (h - 2) * (w - 2) - sum(cnt)
print(*cnt, sep='\n')
