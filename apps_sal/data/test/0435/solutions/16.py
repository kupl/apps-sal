from sys import *


def inp():
    return stdin.readline()


def solve(x, s, n, k):
    (ans, r, bal) = (0, 0, 0)
    for l in range(n):
        while r < n and (s[r] == x or bal < k):
            if s[r] != x:
                bal += 1
            r += 1
        ans = max(ans, r - l)
        if s[l] != x:
            bal -= 1
    return ans


def main():
    (n, k) = map(int, inp().split())
    s = inp()
    print(max(solve('a', s, n, k), solve('b', s, n, k)))


def __starting_point():
    main()


__starting_point()
