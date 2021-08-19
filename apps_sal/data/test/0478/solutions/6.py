import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def solve():
    n = mint()
    i = 0
    s = [0] * n
    for c in minp():
        s[i] = ord(c) - ord('a')
        i += 1
    for c in range(25, 0, -1):
        i = 0
        while i < len(s):
            if s[i] == c and (i > 0 and s[i - 1] == c - 1 or (i + 1 < len(s) and s[i + 1] == c - 1)):
                s.pop(i)
                if i > 0:
                    i -= 1
            else:
                i += 1
    print(n - len(s))


solve()
