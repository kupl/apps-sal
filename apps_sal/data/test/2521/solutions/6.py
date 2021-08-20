from heapq import heappop, heapify, heappush
import sys
INF = 10 ** 20
input = sys.stdin.readline
sys.setrecursionlimit(100000000)
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)


def main():
    n = int(input())
    a = list(map(int, input().split()))
    lM = [0] * (n + 1)
    rm = [0] * (n + 1)
    q = []
    cumsum = 0
    for i in range(n):
        heappush(q, a[i])
        cumsum += a[i]
    lM[0] = cumsum
    drop = 0
    for i in range(n, 2 * n):
        heappush(q, a[i])
        drop += heappop(q)
        cumsum += a[i]
        lM[i - n + 1] = cumsum - drop
    q = []
    cumsum = 0
    for i in range(3 * n - 1, 2 * n - 1, -1):
        heappush(q, -a[i])
        cumsum += a[i]
    rm[-1] = cumsum
    drop = 0
    for i in range(2 * n - 1, n - 1, -1):
        heappush(q, -a[i])
        drop -= heappop(q)
        cumsum += a[i]
        rm[i - n] = cumsum - drop
    ans = -INF
    for i in range(n + 1):
        ans = max(ans, lM[i] - rm[i])
    print(ans)


def __starting_point():
    main()


__starting_point()
