h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
bomb_count = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == "
        continue
        else:
            for k in range(3):
                for l in range(3):
                    a = i - 1 + k
                    b = j - 1 + l
                    if a < 0:
                        continue
                    elif a > h - 1:
                        continue
                    if b < 0:
                        continue
                    elif b > w - 1:
                        continue
                    if s[a][b] == "
                    bomb_count += 1
            s[i][j] = str(bomb_count)
            bomb_count = 0
for i in range(h):
    print("".join(s[i]))
