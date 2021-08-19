import sys
import math
import collections
import bisect
import itertools
sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
MOD = 10 ** 9 + 7


def ni():
    return int(sys.stdin.readline().rstrip())


def ns():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def na():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def na1():
    return list([int(x) - 1 for x in sys.stdin.readline().rstrip().split()])


def main():
    (n, k) = ns()
    pos = []
    for _ in range(n):
        (x, y) = ns()
        pos.append((x, y))
    ans = INF
    for tmp in itertools.combinations_with_replacement(pos, 4):
        xl = max(tmp, key=lambda t: t[0])[0]
        xs = min(tmp, key=lambda t: t[0])[0]
        yl = max(tmp, key=lambda t: t[1])[1]
        ys = min(tmp, key=lambda t: t[1])[1]
        cnt = 0
        for (xi, yi) in pos:
            if xs <= xi <= xl and ys <= yi <= yl:
                cnt += 1
        if cnt >= k:
            ans = min(ans, (xl - xs) * (yl - ys))
    print(ans)


def __starting_point():
    main()


__starting_point()
