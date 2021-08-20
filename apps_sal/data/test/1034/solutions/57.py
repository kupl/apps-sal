import heapq
import sys
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    (X, Y, Z, K) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    def bfs():
        used = set()
        used.add((0, 0, 0))
        q = []
        heapq.heapify(q)
        heapq.heappush(q, (-(A[0] + B[0] + C[0]), 0, 0, 0))
        res = []
        while q:
            (v, i, j, k) = heapq.heappop(q)
            res.append(-v)
            if len(res) == K:
                return res
            for (di, dj, dk) in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
                ni = i + di
                nj = j + dj
                nk = k + dk
                if ni >= X or nj >= Y or nk >= Z:
                    continue
                if (ni, nj, nk) in used:
                    continue
                used.add((ni, nj, nk))
                heapq.heappush(q, (-(A[ni] + B[nj] + C[nk]), ni, nj, nk))
        return res
    res = bfs()
    res.sort(reverse=True)
    for i in range(K):
        print(res[i])


def __starting_point():
    main()


__starting_point()
