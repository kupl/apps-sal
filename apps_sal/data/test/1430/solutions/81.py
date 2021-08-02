import sys
import numpy as np
def input(): return sys.stdin.readline().rstrip()
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())


def main():
    n, k = mi()
    s = input()
    a = [0]
    for i in range(1, n):
        if s[i] != s[i - 1]:
            a.append(i)
    a.append(n)
    ans = 0
    i, e = 0, 0
    m = len(a)
    for i in range(m):
        e = i + 2 * k
        if s[a[i]] == '1':
            e += 1
        e = min(e, m - 1)
        ans = max(ans, a[e] - a[i])
        if e == m - 1:
            break
    print(ans)


def __starting_point():
    main()


__starting_point()
