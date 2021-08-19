
from collections import deque
import sys

sys.setrecursionlimit(10 ** 7)


def resolve():
    def bfs(sy, sx):
        q = deque()
        q.append((sy, sx))
        dist = [[-1] * (W + 2) for _ in range(H + 2)]
        dist[sy][sx] = 0
        drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while q:
            sy, sx = q.popleft()
            for dy, dx in drc:
                ny = dy + sy
                nx = dx + sx
                if G[ny][nx] == "." and dist[ny][nx] == -1:
                    dist[ny][nx] = dist[sy][sx] + 1
                    q.append((ny, nx))

            if not q:
                return dist[sy][sx]

    H, W = list(map(int, input().split()))
    G = []
    G.append(["#"] * (W + 2))
    G += [["#"] + list(input()) + ["#"] for _ in range(H)]
    G.append(["#"] * (W + 2))

    ans = 0
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if G[i][j] == "#":
                continue
            ans = max(ans, bfs(i, j))

    print(ans)


def __starting_point():
    resolve()


__starting_point()
