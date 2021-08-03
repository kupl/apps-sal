import sys
import math


def input():
    return sys.stdin.readline()[:-1]


def main():
    n, k = list(map(int, input().split()))
    s = input()
    c = set(input().split())
    prev = 0
    ans = 0
    for k in range(n):
        if s[k] not in c:
            l = k - prev
            ans += (l * (l + 1)) // 2
            prev = k + 1
    l = k - prev + 1
    ans += (l * (l + 1)) // 2
    print(ans)


def __starting_point():
    main()


__starting_point()
