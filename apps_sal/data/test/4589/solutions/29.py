(H, W) = map(int, input().split())
S = [['' for w in range(W)] for h in range(H)]
for h in range(H):
    S[h] = list(input())
for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            continue
        ymin = max(0, h - 1)
        ymax = min(H, h + 2)
        xmin = max(0, w - 1)
        xmax = min(W, w + 2)
        S[h][w] = 0
        for y in range(ymin, ymax):
            S[h][w] += S[y][xmin:xmax].count('#')
for h in range(H):
    for w in range(W):
        print(S[h][w], end='')
    print('')
