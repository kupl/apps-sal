h, w = map(int, input().split())
s = ["." * (w + 2)]
for i in range(h):
    s.append("." + input() + ".")
s.append("." * (w + 2))
dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [1, 1, 1, 0, -1, -1, -1, 0]
ans = []
for i in range(1, h + 1):
    wp = ""
    for j in range(1, w + 1):
        if s[i][j] == "
        wp += "
        continue
        count = 0
        for k in range(8):
            if s[i + dy[k]][j + dx[k]] == "
            count += 1
        wp += str(count)
    ans.append(wp)
print(*ans, sep="\n")
