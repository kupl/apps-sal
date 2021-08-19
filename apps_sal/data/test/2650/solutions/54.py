import sys
from heapq import heappush, heappop
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (N, Q) = map(int, readline().split())
    M = 2 * 10 ** 5
    p = [[] for _ in range(M)]
    p_del = [[] for _ in range(M)]
    q = []
    q_del = []
    A = [0] * N
    B = [0] * N
    for i in range(N):
        (a, b) = map(int, readline().split())
        A[i] = a
        B[i] = b - 1
        heappush(p[b - 1], -a)
    for i in range(M):
        if p[i]:
            heappush(q, -p[i][0])
    CD = map(int, read().split())
    ans = [0] * Q
    for (i, (c, d)) in enumerate(zip(*[iter(CD)] * 2)):
        c -= 1
        d -= 1
        (b, B[c]) = (B[c], d)
        max_prev = set()
        max_prev.add(-p[b][0])
        if p[d]:
            max_prev.add(-p[d][0])
        heappush(p_del[b], -A[c])
        heappush(p[d], -A[c])
        while p_del[b] and p[b][0] == p_del[b][0]:
            heappop(p[b])
            heappop(p_del[b])
        max_current = set()
        max_current.add(-p[d][0])
        if p[b]:
            max_current.add(-p[b][0])
        for rating in max_prev - max_current:
            heappush(q_del, rating)
        for rating in max_current - max_prev:
            heappush(q, rating)
        while q_del and q[0] == q_del[0]:
            heappop(q)
            heappop(q_del)
        ans[i] = q[0]
    print(*ans, sep='\n')
    return


def __starting_point():
    main()


__starting_point()
