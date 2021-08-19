from heapq import heappop, heappush
import sys
stdin = sys.stdin
sys.setrecursionlimit(10 ** 7)


def li():
    return map(int, stdin.readline().split())


def li_():
    return map(lambda x: int(x) - 1, stdin.readline().split())


def lf():
    return map(float, stdin.readline().split())


def ls():
    return stdin.readline().split()


def ns():
    return stdin.readline().rstrip()


def lc():
    return list(ns())


def ni():
    return int(stdin.readline())


def nf():
    return float(stdin.readline())


bigger = []
smaller = []


def modify(bigger, smaller, a: int, b: int, mid: int, ans: int):
    if not bigger and (not smaller):
        heappush(smaller, -a)
        mid = a
    elif not bigger:
        if a < -smaller[0]:
            heappush(bigger, -heappop(smaller))
            heappush(smaller, -a)
            ans += abs(-smaller[0] - mid)
        else:
            heappush(bigger, a)
    else:
        if a < -smaller[0]:
            tmp = -heappop(smaller)
            heappush(smaller, -a)
            if (len(smaller) + len(bigger)) % 2:
                ans += abs(-smaller[0] - mid)
        elif a > bigger[0]:
            tmp = heappop(bigger)
            heappush(bigger, a)
        else:
            tmp = a
        if len(smaller) == len(bigger):
            heappush(smaller, -tmp)
        else:
            heappush(bigger, tmp)
    ans += abs(-smaller[0] - a) + b
    mid = -smaller[0]
    return (mid, ans)


q = ni()
mid = ans = 0
for _ in range(q):
    query = ns()
    if query.startswith('1'):
        (_, a, b) = map(int, query.split())
        (mid, ans) = modify(bigger, smaller, a, b, mid, ans)
    else:
        print(mid, ans)
