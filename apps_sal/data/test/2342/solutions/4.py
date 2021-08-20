import sys


def input():
    return sys.stdin.readline().rstrip('\n')


D = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def case():
    (n, m) = list(map(int, input().split()))
    M = [list(input()) for _ in range(n)]
    good = set()
    for y in range(n):
        for x in range(m):
            c = M[y][x]
            if c == 'G':
                good.add((x, y))
            elif c == 'B':
                for (dx, dy) in D:
                    nx = x + dx
                    ny = y + dy
                    if nx < 0 or ny < 0 or nx >= m or (ny >= n):
                        continue
                    if M[ny][nx] == 'G':
                        print('No')
                        return
                    elif M[ny][nx] != 'B':
                        M[ny][nx] = '#'
    if M[-1][-1] == '#':
        print('No' if good else 'Yes')
        return
    V = [[False] * m for _ in range(n)]
    V[n - 1][m - 1] = True
    Q = [(m - 1, n - 1)]
    while Q:
        (x, y) = Q.pop()
        good.discard((x, y))
        for (dx, dy) in D:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= m or (ny >= n):
                continue
            if M[ny][nx] == '#' or V[ny][nx]:
                continue
            V[ny][nx] = True
            Q.append((nx, ny))
    print('Yes' if not good else 'No')


for _ in range(int(input())):
    case()
