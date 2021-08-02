def main():
    from collections import deque
    import sys
    input = sys.stdin.readline

    M = 10 ** 5

    N = int(input())

    g = tuple(set() for _ in range(M * 2))
    ps = set()
    for _ in range(N):
        x, y = (int(x) - 1 for x in input().split())  # 一律に移動
        g[x].add(y + M)
        g[y + M].add(x)
        ps.add(x)
        ps.add(y + M)

    visited = [0] * (M * 2)
    ans = 0
    for s in ps:
        if visited[s]:
            continue
        visited[s] = 1
        dq = deque()
        dq.append(s)

        sz = 0
        x = 0
        while dq:
            v = dq.popleft()
            sz += 1
            if v < M:
                x += 1
            for u in g[v]:
                if visited[u]:
                    continue
                visited[u] = 1
                dq.append(u)
        ans += (sz - x) * x

    ans -= N

    print(ans)


def __starting_point():
    main()

# 連結成分ごとに
# x,yの二部グラフを完全二部グラフにする
# cnt(x)*cnt(y)-既存の辺数の総和

# 最後にN引けばよい


__starting_point()
