import sys
from collections import Counter


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = Counter(list(map(int, input().split())))
    ans = 0
    for (k, v) in a.items():
        if k < v:
            ans += v - k
        elif k > v:
            ans += v
    print(ans)


def __starting_point():
    main()


__starting_point()
