import sys
import copy
import heapq
from collections import deque
def input(): return sys.stdin.readline().rstrip()


INF = 10**9 + 7


def solve():
    N, K = list(map(int, input().split()))
    V = deque(list(map(int, input().split())))

    ans = -INF
    for n in range(1, N + 1):
        if n > K:
            break
        for rn in range(n + 1):
            ln = n - rn
            tv = copy.copy(V)
            pv = 0
            mv = []
            heapq.heapify(mv)
            for _ in range(rn):
                v = tv.pop()
                if v >= 0:
                    pv += v
                else:
                    heapq.heappush(mv, v)
            for _ in range(ln):
                v = tv.popleft()
                if v >= 0:
                    pv += v
                else:
                    heapq.heappush(mv, v)

            mvlen = min(K - n, len(mv))
            for _ in range(0, mvlen):
                heapq.heappop(mv)

            ans = max(ans, pv + sum(mv))

    print((max(0, ans)))


def __starting_point():
    solve()


__starting_point()
