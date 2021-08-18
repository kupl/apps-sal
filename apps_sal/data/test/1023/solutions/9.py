import sys
from bisect import bisect_left
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())


def __starting_point():

    n, m, ta, tb, k = mi()
    a = lmi()
    b = lmi()
    if n <= k or m <= k:
        print(-1)
        return
    a = [i + ta for i in a]
    lenb = len(b)
    a.sort()
    b.sort()
    ans = -10**9
    for i in range(k + 1):
        if bisect_left(b, a[i]) + (k - i) >= lenb:
            print(-1)
            return
        else:
            ans = max(ans, b[bisect_left(b, a[i]) + (k - i)])
    print(ans + tb)


__starting_point()
