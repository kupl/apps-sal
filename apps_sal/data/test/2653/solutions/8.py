def abc138d_ki():
    import heapq
    n, q = map(int, input().split())
    cnt = [0] * n
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    for _ in range(q):
        p, x = map(int, input().split())
        cnt[p - 1] += x
    qu = [(0, 0)]
    heapq.heapify(qu)
    check = [False] * n
    while len(qu) != 0:
        h, no = heapq.heappop(qu)
        check[no] = True
        for nxt in graph[no]:
            if not check[nxt]:
                cnt[nxt] += cnt[no]
                heapq.heappush(qu, (h + 1, nxt))
    for c in cnt:
        print(c, end=' ')


abc138d_ki()
