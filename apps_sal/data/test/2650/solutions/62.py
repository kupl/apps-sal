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
    hq1 = [[] for _ in range(M)]
    hq2 = [[] for _ in range(M)]
    hq_ans1 = []
    hq_ans2 = []
    A = [0] * N
    B = [0] * N
    for i in range(N):
        (a, b) = map(int, readline().split())
        A[i] = a
        B[i] = b - 1
        heappush(hq1[b - 1], -a)
    for i in range(M):
        if hq1[i]:
            heappush(hq_ans1, -hq1[i][0])
    CD = map(int, read().split())
    ans = [0] * Q
    for (i, (c, d)) in enumerate(zip(*[iter(CD)] * 2)):
        c -= 1
        d -= 1
        b = B[c]
        B[c] = d
        max_from_prev = -hq1[b][0]
        if hq1[d]:
            max_to_prev = -hq1[d][0]
        else:
            max_to_prev = None
        heappush(hq2[b], -A[c])
        heappush(hq1[d], -A[c])
        while hq2[b] and hq1[b][0] == hq2[b][0]:
            heappop(hq1[b])
            heappop(hq2[b])
        if hq1[b]:
            max_from = -hq1[b][0]
        else:
            max_from = None
        max_to = -hq1[d][0]
        if max_from_prev != max_from:
            heappush(hq_ans2, max_from_prev)
            if max_from:
                heappush(hq_ans1, max_from)
        if max_to_prev != max_to:
            if max_to_prev:
                heappush(hq_ans2, max_to_prev)
            heappush(hq_ans1, max_to)
        while hq_ans2 and hq_ans1[0] == hq_ans2[0]:
            heappop(hq_ans1)
            heappop(hq_ans2)
        ans[i] = hq_ans1[0]
    print(*ans, sep='\n')
    return


def __starting_point():
    main()


__starting_point()
