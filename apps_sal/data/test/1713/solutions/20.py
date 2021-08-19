"""http://codeforces.com/problemset/problem/285/B"""


def solve(n, s, t, p):
    p.insert(0, 0)
    for i in range(n + 1):
        if s == t:
            return i
        s = p[s]
    return -1


def __starting_point():
    (n, s, t) = list(map(int, input().split()))
    p = list(map(int, input().split()))
    res = solve(n, s, t, p)
    print(res)


__starting_point()
