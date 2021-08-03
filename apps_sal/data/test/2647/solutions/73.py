from collections import deque
from typing import List


def main():
    h, w = list(map(int, input().split()))
    g = []
    for _ in range(h):
        gg = list(input())
        g.append(gg)
    print((gr(h, w, g)))


def gr(h: int, w: int, g: List[List[str]]) -> int:
    m = [[-1] * w for _ in range(h)]
    q = deque([(0, 0)])
    m[0][0] = 0
    while q:
        x, y = q.popleft()
        for nx, ny in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            if (0 <= nx <= w - 1 and 0 <= ny <= h - 1) and g[ny][nx] == "." and m[ny][nx] < 0:
                m[ny][nx] = m[y][x] + 1
                if nx == w - 1 and ny == h - 1:
                    break
                q.append((nx, ny))

    if m[h - 1][w - 1] < 0:
        return -1
    return sum(gg.count(".") for gg in g) - m[h - 1][w - 1] - 1


def __starting_point():
    main()


__starting_point()
