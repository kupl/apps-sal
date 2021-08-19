import sys
from collections import deque
input = sys.stdin.readline


def bfs(S, sh, sw, dist):
    dist[sh][sw] = 0
    queue = deque([(sh, sw)])
    while queue:
        (h, w) = queue.popleft()
        for (i, j) in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            (y, x) = (h + i, w + j)
            if S[y][x] == '#':
                continue
            if dist[y][x] == -1:
                dist[y][x] = dist[h][w] + 1
                queue.append((y, x))


def main():
    (H, W) = list(map(int, input().split()))
    S = [None] * (H + 2)
    S[0] = S[-1] = '#' * (W + 2)
    for i in range(1, H + 1):
        S[i] = ''.join(['#', input().rstrip(), '#'])
    ans = 0
    for sh in range(1, H + 1):
        for sw in range(1, W + 1):
            if S[sh][sw] == '#':
                continue
            dist = [[-1] * (W + 2) for _ in range(H + 2)]
            bfs(S, sh, sw, dist)
            max_dist = max(list(map(max, dist)))
            ans = max(ans, max_dist)
    print(ans)


def __starting_point():
    main()


__starting_point()
