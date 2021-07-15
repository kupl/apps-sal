c = [int(i) for i in input().split()]
a = [ord(x) - ord('a') for x in input()]
n = len(a)
l = [[] for i in range(26)]
r = [[] for i in range(26)]
s = 0
ans = 0
for i in range(n-1):
    s += c[a[i]]
    l[a[i]] += [(s, i)]
    r[a[i+1]] += [(s, i)]
for i in range(26):
    n, m = len(l[i]), len(r[i])
    if n < 1 or m < 1: continue
    l[i].sort()
    r[i].sort()
    a[m - 1] = m - 1
    for j in range(m - 2, -1, -1):
        if r[i][j][0] == r[i][j+1][0]:
            a[j] = a[j+1]
        else:
            a[j] = j
    y = 0
    for j in range(n):
        while y < m and r[i][y][0] < l[i][j][0]: y += 1
        while y < m and r[i][y][0] == l[i][j][0] and r[i][y][1] < l[i][j][1]: y += 1
        if y == m: break
        if r[i][y][0] == l[i][j][0]:
            ans += a[y] - y + 1
print(ans)
