import heapq


def main():
    N, M = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = list(map(int, input().split()))
        G[a - 1].append((b - 1, c))
        G[b - 1].append((a - 1, c))
    used = set()
    for i in range(N):
        H = []
        for b, c in G[i]:
            heapq.heappush(H, (c, i, b))
        D = [10**10] * N
        D[i] = 0
        while H:
            c, a, b = heapq.heappop(H)
            if D[b] < c:
                continue
            D[b] = c
            if a < b:
                used.add((a, b))
            else:
                used.add((b, a))
            for d, cc in G[b]:
                if D[d] > c + cc:
                    D[d] = c + cc
                    heapq.heappush(H, (c + cc, b, d))
    return M - len(used)


print((main()))
