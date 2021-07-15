t = input;p = print;r = range
n, m = map(int, t().split())
a, x, y, c =  [], [0]*n, [0]*m, 0
for i in r(n):
    a.append(t())
    for j in r(m):
        if a[i][j] == "*":
            x[i], y[j], c = x[i] + 1, y[j] + 1, c + 1
for i in r(n):
    for j in r(m):
        if x[i] + y[j] - (a[i][j] == "*") == c: p("YES\n{0} {1}".format(i + 1, j + 1));return
p("NO")

