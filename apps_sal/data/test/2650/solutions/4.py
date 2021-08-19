import sys
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    MAX = 10 ** 5 * 2
    (N, Q) = list(map(int, input().split()))
    heap = [[] for _ in range(MAX)]
    for i in range(MAX):
        heapq.heapify(heap[i])
    rates = [0] * N
    places = [0] * N
    for i in range(N):
        (a, b) = list(map(int, input().split()))
        places[i] = b - 1
        rates[i] = a
        heapq.heappush(heap[b - 1], (-a, i))
    heap_all = []
    heapq.heapify(heap_all)
    m = INF
    p = None
    for i in range(MAX):
        if not heap[i]:
            continue
        m = -heap[i][0][0]
        p = i
        child = heap[i][0][1]
        heapq.heappush(heap_all, (m, p, child))
    ans = []
    for _ in range(Q):
        (c, d) = list(map(int, input().split()))
        child = c - 1
        cur = d - 1
        prev = places[child]
        rate = rates[child]
        heapq.heappush(heap[cur], (-rate, child))
        places[child] = cur
        while heap[prev]:
            (v, i) = heap[prev][0]
            if places[i] == prev:
                heapq.heappush(heap_all, (-v, prev, i))
                break
            else:
                heapq.heappop(heap[prev])
        while heap[cur]:
            (v, i) = heap[cur][0]
            if places[i] == cur:
                heapq.heappush(heap_all, (-v, cur, i))
                break
            else:
                heapq.heappop(heap[cur])
        while True:
            (r, p, i) = heap_all[0]
            if p == places[i] and heap[p][0][0] == -r:
                ans.append(r)
                break
            else:
                heapq.heappop(heap_all)
    for a in ans:
        print(a)


def __starting_point():
    main()


__starting_point()
