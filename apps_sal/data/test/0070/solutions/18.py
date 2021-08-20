import math
import sys


def main():
    s = input().split()
    k = int(s[1])
    n = s[0]
    l = len(n)
    ans = 0
    for i in range(l):
        if i - ans == k:
            print(ans)
            return
        if n[l - i - 1] != '0':
            ans += 1
    if l - ans > 0:
        print(l - 1)


def __starting_point():
    main()


__starting_point()
