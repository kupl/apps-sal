def f():
    s = input().split()
    m = int(s[0])
    n = int(s[1])
    ss = []
    for i in range(m):
        ss.append(input())
    for i in range(m):
        for j in range(n):
            if ss[i][j] == 'X':
                return (ss, m, n, i, j)


def ff(ss, m, n):
    for k in range(m - 1, -1, -1):
        for l in range(n - 1, -1, -1):
            if ss[k][l] == 'X':
                return (k, l)


ss, m, n, i, j = f()
k, l = ff(ss, m, n)
sss = []
for x in range(m):
    s = ""
    for y in range(n):
        if (i <= x and x <= k and j <= y and y <= l):
            s += "X"
        else:
            s += "."
    sss.append(s)
if(ss == sss):
    print("YES")
else:
    print("NO")
