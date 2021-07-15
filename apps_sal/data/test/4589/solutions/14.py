from itertools import product
h, w = map(int, input().split())
G = [list(input()) for _ in range(h)]
for y, x in product(range(h), range(w)):
    if G[y][x]=='.':
        G[y][x]=0
        for dy, dx in product(range(-1, 2), repeat=2):
            ny = y+dy
            nx = x+dx
            if 0 <= ny < h and 0 <= nx < w:
                G[y][x] += G[ny][nx]=='#'
for g in G:
    print(*g, sep='')

