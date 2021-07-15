import sys
from collections import deque


def solve():
    N, M = map(int, input().split())
    edges = [set() for _ in range(N+1)]
    for a, b in (map(int, line.split()) for line in sys.stdin):
        edges[a].add(b)

    # 答えが見つかるまで、スタート地点は全て試します
    for start in range(1, N+1):
        visited = [0]*(N+1)

        dq = deque([(start, {start})])
        visited[start] = 1

        while dq:
            # 点と、これまで通ってきた頂点を取り出す
            v, route = dq.popleft()
            # これまで通ってきた頂点集合と、行き先の頂点集合の積集合をとる
            s = route & edges[v]
            # s=={start}でなければuとおr sが空集合でも通る。sが何やらいろいろあると、通れない。
            if not (not s or s == {start}):
                continue
            for dest in edges[v]:
                # startに戻ってきたら出力して終了
                if dest == start:
                    print(len(route))
                    print(*route, sep='\n')
                    return
                # 訪問済みであれば、スルー
                if visited[dest]:
                    continue
                visited[dest] = 1
                # destを始点として、通ってきた頂点にdestを追加したもの
                dq.append((dest, route | {dest}))

    print(-1)


def __starting_point():
    solve()

__starting_point()
