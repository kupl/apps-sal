
DELTAS = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1),
}

try:
    while True:
        h, w, y, x = map(int, input().split())
        y -= 1
        x -= 1
        s = input()
        total = h * w - 1
        used = [[False] * w for i in range(h)]
        used[y][x] = True
        print(end="1 ")
        last = len(s) - 1
        for i, c in enumerate(s):
            dy, dx = DELTAS[c]
            ny = y + dy
            nx = x + dx
            if 0 <= ny < h and 0 <= nx < w:
                if i != last:
                    if used[ny][nx]:
                        print(end="0 ")
                    else:
                        print(end="1 ")
                        used[ny][nx] = True
                        total -= 1
                y = ny
                x = nx
            elif i != last:
                print(end="0 ")
        print(total)

except EOFError:
    pass
