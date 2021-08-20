import math
import sys
import itertools


def main():
    (n, k) = map(int, input().split())
    lst = input().split()
    d = []
    it = 0
    itd = 0
    for i in range(k):
        if it > 25:
            itd += 1
            it = 0
        d.append(chr(65 + itd) + chr(97 + it))
        it += 1
    ans = []
    for i in range(k - 1):
        ans.append(d.pop())
    for i in range(k - 1, n):
        if lst[i - (k - 1)] == 'NO':
            ans.append(ans[i - (k - 1)])
        else:
            ans.append(d.pop())
            d.append(ans[i - (k - 1)])
    for i in range(n):
        print(ans[i], end=' ')
    print()


def __starting_point():
    main()


__starting_point()
