# O(klog(k))解法 多分...
import sys
from heapq import heappush, heapify, heappop
input = sys.stdin.readline


def make_kth(A, B, k):
    n, m = len(A), len(B)
    q = [(-A[0] - B[0], 0, 0)]
    r = []
    for _ in range(min(k, n * m)):
        v, s, t = heappop(q)
        r.append(-v)
        if t + 1 < m:
            heappush(q, (-A[s] - B[t + 1], s, t + 1))
        if t == 0 and s + 1 < n:
            heappush(q, (-A[s + 1] - B[0], s + 1, 0))
    return r


def main():
    _, _, _, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    a.sort(reverse=1)
    b.sort(reverse=1)
    c.sort(reverse=1)

    r = make_kth(a, b, k)
    r = make_kth(c, r, k)
    print(*r, sep="\n")


main()
