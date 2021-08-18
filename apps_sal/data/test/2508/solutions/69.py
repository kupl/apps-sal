
from collections import deque
H, W, K = map(int, input().split())
sth, stw, glh, glw = map(int, input().split())
sth, stw = sth - 1, stw - 1
glh, glw = glh - 1, glw - 1

INF = -1
Gmap = [list(input()) for _ in range(H)]
Seen = [[INF] * W for _ in range(H)]
direc = {(1, 0), (-1, 0), (0, 1), (0, -1)}


def bfs(sth, stw, glh, glw):
    next_q = deque([])
    next_q.append((sth, stw, 0))
    Seen[sth][stw] = 0

    while len(next_q) != 0:
        h, w, c = next_q.popleft()
        for dh, dw in direc:
            for sk in range(1, K + 1):
                hs, ws = h + dh * sk, w + dw * sk
                if not (0 <= hs < H and 0 <= ws < W):
                    break
                if Gmap[hs][ws] == '@':
                    break
                if Seen[hs][ws] == INF:
                    next_q.append((hs, ws, c + 1))
                    Seen[hs][ws] = c + 1
                elif Seen[hs][ws] <= c:
                    break
                if hs == glh and ws == glw:
                    return c + 1
    return -1


def main():
    ret = bfs(sth, stw, glh, glw)
    print(ret)


def __starting_point():
    main()


__starting_point()
