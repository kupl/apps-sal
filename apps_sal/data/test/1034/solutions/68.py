import sys
input = sys.stdin.readline
import heapq
from collections import defaultdict


def read():
    X, Y, Z, K = list(map(int, input().strip().split()))
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    C = list(map(int, input().strip().split()))
    return X, Y, Z, K, A, B, C


def solve(X, Y, Z, K, A, B, C, INF=10000000001):
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    
    used = defaultdict(bool)
    h = []
    p, q, r = 0, 0, 0
    heapq.heappush(h, (-A[p] - B[q] - C[r], p, q, r))
    used[(p, q, r)] = True
    for k in range(K):
        a, p, q, r = heapq.heappop(h)
        print((-a))
        if p+1 < len(A) and not used[(p+1, q, r)]:
            heapq.heappush(h, (-A[p+1] - B[q] - C[r], p+1, q, r))
            used[(p+1, q, r)] = True
        if q+1 < len(B) and not used[(p, q+1, r)]:
            heapq.heappush(h, (-A[p] - B[q+1] - C[r], p, q+1, r))
            used[(p, q+1, r)] = True
        if r+1 < len(C) and not used[(p, q, r+1)]:
            heapq.heappush(h, (-A[p] - B[q] - C[r+1], p, q, r+1))
            used[(p, q, r+1)] = True


def __starting_point():
    inputs = read()
    solve(*inputs)

__starting_point()
