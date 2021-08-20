import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    (x, y, a, b, c) = list(map(int, input().split()))
    p = sorted(list(map(int, input().split())), reverse=True)[0:x]
    q = sorted(list(map(int, input().split())), reverse=True)[0:y]
    r = sorted(list(map(int, input().split())), reverse=True)
    pq = sorted(p + q)
    for i in range(min(c, x + y)):
        if pq[i] > r[i]:
            break
        pq[i] = r[i]
    print(sum(pq))


def __starting_point():
    main()


__starting_point()
