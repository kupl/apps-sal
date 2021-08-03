h, w = map(int, input().split())
a = [list(input()) for i in range(h)]
delrow = []
delline = []
for i in range(w):
    whiteline = 0
    for j in range(h):
        if a[j][i] == ".":
            whiteline += 1
        if whiteline == h:
            delline.append(i)
for i in range(h):
    whiterow = 0
    for j in range(w):
        if a[i][j] == ".":
            whiterow += 1
        if whiterow == w:
            delrow.append(i)
for i in range(h):
    if i in delrow:
        continue
    else:
        ans = ""
        for j in range(w):
            if j in delline:
                continue
            else:
                ans += a[i][j]
    print(ans)
