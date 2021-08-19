def __starting_point():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N = int(input())
    edges = [[] for _ in range(N)]
    for i in range(N - 1):
        (a, b) = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].append((b, i))
        edges[b].append((a, i))
    color = [None] * (N - 1)
    SIZE = 1
    q = deque([(0, None)])
    while q:
        (v, prev_color) = q.popleft()
        c = 1
        for (w, i) in edges[v]:
            if not color[i]:
                if c == prev_color:
                    c += 1
                color[i] = c
                c += 1
                q.append((w, color[i]))
        SIZE = max(SIZE, c - 1)
    print(SIZE)
    for n in range(N - 1):
        print(color[n])


__starting_point()
