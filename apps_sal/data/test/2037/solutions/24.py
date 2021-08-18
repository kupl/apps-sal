

import sys

inf = float("inf")
mod = 1000000007


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return map(int, sys.stdin.readline().split())


def input(): return sys.stdin.readline()


def main():
    n, m = get_ints()
    arr = get_array()
    d = {}
    s = set()
    ans = [0] * m
    for i in range(m):
        x = arr[i]
        if x not in d:
            d[x] = 0
        d[x] += 1
        s.add(x)
        if len(s) == n:
            ans[i] = 1
            for i in range(1, n + 1):
                d[i] -= 1
                if d[i] == 0:
                    s.remove(i)
        else:
            ans[i] = 0
    print(*ans, sep='')


def __starting_point():
    main()


__starting_point()
