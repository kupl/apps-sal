from collections import deque

n = int(input())
y1, x1 = list(map(int, input().split(' ')))
y2, x2 = list(map(int, input().split(' ')))
y1 -= 1
x1 -= 1
y2 -= 1
x2 -= 1

dat = [input() for _ in range(n)]

bfs1 = [-1] * ((n + 1) * (n + 1))
bfs2 = [-1] * ((n + 1) * (n + 1))


def bfs(res, ys, xs):
    nonlocal dat, n
    d = deque()
    d.append([ys, xs, 0])

    while len(d) != 0:
        y, x, pr = d.popleft()

        if y == -1 or x == -1 or y >= n or x >= n:
            continue

        if dat[y][x] == '1':
            continue

        id = y * n + x
        if res[id] != -1 and res[id] <= pr:
            continue

        res[id] = pr
        pr += 1
        d.append([y + 0, x - 1, pr])
        d.append([y + 0, x + 1, pr])
        d.append([y - 1, x + 0, pr])
        d.append([y + 1, x + 0, pr])


bfs(bfs1, y1, x1)
bfs(bfs2, y2, x2)

if bfs1[y2 * n + x2] != -1:
    print(0)
    return

best = 1000000000000


def pow2(x):
    return x * x


for ys in range(n):
    for xs in range(n):
        ids = ys * n + xs
        if bfs1[ids] == -1:
            continue

        for ye in range(n):
            for xe in range(n):
                ide = ye * n + xe
                if bfs2[ide] == -1:
                    continue

                price = pow2(xs - xe) + pow2(ys - ye)
                best = min(best, price)

print(best)
