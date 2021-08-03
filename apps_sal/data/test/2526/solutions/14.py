def main():
    import heapq
    x, y, a, b, c = list(map(int, input().split()))
    p = sorted(list(map(int, input().split())), reverse=True)[0:x]
    q = sorted(list(map(int, input().split())), reverse=True)[0:y]
    r = sorted(list(map(int, input().split())), reverse=True)
    P, Q = [], []
    for i in range(x):
        heapq.heappush(P, p[i])
    for i in range(y):
        heapq.heappush(Q, q[i])
    for i in range(c):
        p, q = heapq.heappop(P), heapq.heappop(Q)
        if p > q:
            heapq.heappush(P, p)
            if r[i] > q:
                heapq.heappush(Q, r[i])
            else:
                heapq.heappush(Q, q)
        else:
            heapq.heappush(Q, q)
            if r[i] > p:
                heapq.heappush(P, r[i])
            else:
                heapq.heappush(P, p)
    print((sum(P) + sum(Q)))


def __starting_point():
    main()


__starting_point()
