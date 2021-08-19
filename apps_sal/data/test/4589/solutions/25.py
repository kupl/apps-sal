h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            c = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    else:
                        if 0 <= i + y and 0 <= j + x and i + y < h and j + x < w:
                            if s[i + y][j + x] == "#":
                                c += 1
            s[i][j] = str(c)
for a in range(h):
    print("".join(s[a]))
