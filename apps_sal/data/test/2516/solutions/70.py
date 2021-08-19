import math
import queue
from collections import deque, defaultdict
import heapq as hpq
from sys import stdin, setrecursionlimit
ipt = stdin.readline
setrecursionlimit(10 ** 7)


def main():
    (n, p) = list(map(int, ipt().split()))
    s = input()
    ans = 0
    if p == 2:
        for i in range(n):
            if int(s[i]) % 2 == 0:
                ans += i + 1
        print(ans)
    elif p == 5:
        for i in range(n):
            if int(s[i]) % 5 == 0:
                ans += i + 1
        print(ans)
    else:
        d = defaultdict(int)
        pi = 0
        nk = 10 % p
        for i in s[::-1]:
            pi = (pi + int(i) * nk) % p
            d[pi] += 1
            nk = nk * 10 % p
        for i in list(d.values()):
            ans += i * (i - 1) // 2
        ans += d[0]
        print(ans)
    return


def __starting_point():
    main()


__starting_point()
