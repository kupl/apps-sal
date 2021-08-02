n, m = list(map(int, input().split()))
a = []
for i in range(n):
    s = input().split()
    a.append(s)
for i in range(n):
    for j in range(m):
        if a[i][0][j] == "S":
            k = j
            l = i
            continue
s = "s"
x = k
y = l
if k == 0:
    k = 1
else:
    k = 0
while a[l][0][k] != "S":
    if y > 0:
        if ((a[y - 1][0][x] == "*") or (a[y - 1][0][x] == "S")) and (s[len(s) - 1] != "D"):
            s += "U"
            y -= 1
    if y < n - 1:
        if ((a[y + 1][0][x] == "*") or (a[y + 1][0][x] == "S")) and (s[len(s) - 1] != "U"):
            s += "D"
            y += 1
    if x > 0:
        if ((a[y][0][x - 1] == "*") or (a[y][0][x - 1] == "S")) and (s[len(s) - 1] != "R"):
            s += "L"
            x -= 1
    if x < m - 1:
        if ((a[y][0][x + 1] == "*") or (a[y][0][x + 1] == "S")) and (s[len(s) - 1] != "L"):
            s += "R"
            x += 1
    if a[y][0][x] == "S":
        k = x
        y = l

print(s[1:])
