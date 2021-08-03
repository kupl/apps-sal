#!/usr/bin/env python3

def main():
    n, u, v = list(map(int, input().split()))
    u -= 1
    v -= 1
    adj = [[] for i in range(n)]
    for i in range(n - 1):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        adj[a].append(b)
        adj[b].append(a)

    # uv間経路を求める
    st = [u]
    prev = [None for i in range(n)]
    while st:
        x = st.pop()
        for y in adj[x]:
            if y == prev[x]:
                continue
            prev[y] = x
            st.append(y)
    path = [v]
    while path[-1] != u:
        path.append(prev[path[-1]])
    path = list(reversed(path))

    # crossからsquareを経由しない最遠ノードstarを求める（a59p22）
    l = len(path) - 1
    cross = path[(l - 1) // 2]
    square = path[(l - 1) // 2 + 1]
    st = [(cross, 0)]
    prev = [None for i in range(n)]
    dist = [-1 for i in range(n)]
    while st:
        x, d = st.pop()
        dist[x] = d
        for y in adj[x]:
            if y == prev[x]:
                continue
            if y == square:
                continue
            prev[y] = x
            st.append((y, d + 1))
    star_square = max(dist)

    if l % 2 == 1:
        res = (l - 1) // 2 + star_square
    else:
        res = (l - 1) // 2 + star_square + 1
    print(res)


def __starting_point():
    main()


__starting_point()
