import math
import queue
from collections import deque, defaultdict
import heapq as hpq
from sys import stdin, setrecursionlimit
ipt = stdin.readline
setrecursionlimit(10 ** 7)


def main():
    (n, a, b) = list(map(int, ipt().split()))
    if a * b < n or a + b - 1 > n:
        print(-1)
        return
    ans = [str(b - i) for i in range(b)]
    si = n - a + 2
    ue = n + 1
    i = 0
    while True:
        if si <= b or a == 1:
            break
        ans[i] += ' ' + ' '.join(map(str, list(range(si, ue))))
        ue = si
        si -= a - 1
        i += 1
    if i < b and b + 1 < ue:
        ans[i] += ' ' + ' '.join(map(str, list(range(b + 1, ue))))
    print(' '.join(ans))
    return


def __starting_point():
    main()


__starting_point()
