def main():
    from collections import deque
    import sys
    input = sys.stdin.readline

    M = 10 ** 5

    N = int(input())

    g = tuple(set() for _ in range(M * 2))
    for _ in range(N):
        x, y = (int(x) - 1 for x in input().split())
        g[x].add(y + M)
        g[y + M].add(x)

    visited = [0] * (M * 2)
    ans = 0
    for s in range(M * 2):
        if visited[s]:
            continue
        visited[s] = 1
        dq = deque()
        dq.append(s)

        sz = 0
        x = 0
        e = 0
        while dq:
            v = dq.popleft()
            sz += 1
            if v < M:
                x += 1
            for u in g[v]:
                e += 1
                if visited[u]:
                    continue
                visited[u] = 1
                dq.append(u)
        ans += (sz - x) * x - (e // 2)

    print(ans)


def __starting_point():
    main()


__starting_point()
