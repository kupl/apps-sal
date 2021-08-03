import sys
import heapq
def input(): return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i, n):
            h = [0]
            heapq.heapify(h)
            count = 0
            for p in range(i - 1):
                heapq.heappush(h, v[p])
                count += 1
            for m in range(j + 1, n):
                heapq.heappush(h, v[m])
                count += 1
            while h[0] < 0 and count < k:
                t = heapq.heappop(h)
                count += 1
            if count <= k:
                ans = max(ans, sum(h))
    counts = n
    heapq.heapify(v)
    while h[0] < 0 and counts < k:
        t = heapq.heappop(v)
        counts += 1
    if counts <= k:
        ans = max(ans, sum(v))
    print(ans)


def __starting_point():
    main()


__starting_point()
