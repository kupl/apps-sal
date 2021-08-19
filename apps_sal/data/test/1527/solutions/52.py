from collections import deque
from typing import List


def main():
    (h, w) = list(map(int, input().split()))
    g = []
    for _ in range(h):
        r = list(input())
        g.append(r)
    print(mm(h, w, g))


def mm(h: int, w: int, g: List[List[str]]) -> int:
    ret = 0
    for i in range(h):
        for j in range(w):
            if g[i][j] == '#':
                continue
            v = set()
            q = deque([(i, j, 0)])
            v.add((i, j))
            while q:
                (ii, jj, cnt) = q.popleft()
                ret = max(ret, cnt)
                if ii < h - 1 and g[ii + 1][jj] == '.' and ((ii + 1, jj) not in v):
                    q.append((ii + 1, jj, cnt + 1))
                    v.add((ii + 1, jj))
                if jj < w - 1 and g[ii][jj + 1] == '.' and ((ii, jj + 1) not in v):
                    q.append((ii, jj + 1, cnt + 1))
                    v.add((ii, jj + 1))
                if ii > 0 and g[ii - 1][jj] == '.' and ((ii - 1, jj) not in v):
                    q.append((ii - 1, jj, cnt + 1))
                    v.add((ii - 1, jj))
                if jj > 0 and g[ii][jj - 1] == '.' and ((ii, jj - 1) not in v):
                    q.append((ii, jj - 1, cnt + 1))
                    v.add((ii, jj - 1))
    return ret


def __starting_point():
    main()


__starting_point()
