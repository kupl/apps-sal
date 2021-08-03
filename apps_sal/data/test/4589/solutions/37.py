h, w = list(map(int, input().split()))
s = []
for i in range(h):
    s.append(list(input()))

dx = [1, 0, -1, 0, 1, -1, 1, -1]
dy = [0, 1, 0, -1, 1, 1, -1, -1]

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            continue

        tmp = 0
        for k in range(8):
            ni = i + dx[k]
            nj = j + dy[k]

            if ni < 0 or ni >= h:
                continue
            if nj < 0 or nj >= w:
                continue
            if s[ni][nj] == "#":
                tmp += 1
        s[i][j] = str(tmp)

for i in range(h):
    print(("".join(s[i])))
