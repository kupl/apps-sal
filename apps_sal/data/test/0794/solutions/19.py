import sys
from collections import Counter


def input():
    return sys.stdin.readline().strip()


def rinput():
    return input().split()


def rt(a, s, q):
    if a == s:
        return True
    while a in q:
        a = q[a]
        if a == s:
            return True
    return False


def main():
    input()
    a = sorted(list(map(int, input().split())))
    if a[0] != a[-1]:
        print(*a)
    else:
        print(-1)


main()
