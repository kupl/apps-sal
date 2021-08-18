import sys
import bisect
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, k, A, B = list(map(int, input().split()))
K = list(map(int, input().split()))

K.sort()


def points(l, r):
    if r == l + 1:
        x = bisect.bisect_left(K, r) - bisect.bisect_left(K, l)
        if x != 0:
            return B * x
        else:
            return A

    mid = (l + r) // 2

    x = bisect.bisect_left(K, mid) - bisect.bisect_left(K, l)
    y = bisect.bisect_left(K, r) - bisect.bisect_left(K, mid)

    if x == 0 and y == 0:
        return A
    elif x != 0 and y != 0:
        return points(l, mid) + points(mid, r)
    elif y == 0:
        return min(A + points(l, mid), B * (x + y) * (r - l))
    elif x == 0:
        return min(A + points(mid, r), B * (x + y) * (r - l))


print(points(1, 2**n + 1))
