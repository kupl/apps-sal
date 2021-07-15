import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
from itertools import groupby
from heapq import heappop, heappush, heapify
def resolve():
    n, k, q = map(int, input().split())
    A = list(map(int, input().split()))

    ans = INF
    for m in sorted(A):
        C = []
        for key, it in groupby(A, key = lambda a : a >= m):
            if key is False:
                continue
            D = list(it)
            if len(D) >= k:
                D.sort()
                C.append(D[:len(D) - k + 1][::-1])

        if sum(len(a) for a in C) < q:
            continue
        heap = [(C[i].pop(), i) for i in range(len(C))]
        heapify(heap)
        for _ in range(q):
            M, i = heappop(heap)
            if C[i]:
                heappush(heap, (C[i].pop(), i))
        ans = min(ans, M - m)

    print(ans)
resolve()
