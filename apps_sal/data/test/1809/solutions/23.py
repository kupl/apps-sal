def f(s):
    return int(s) - 1


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(f, input().split()))
c = [[0] * n for i in range(n)]
o = 0
for i in range(m):
    for j in range(n):
        if j != b[i]:
            c[j][b[i]] = 1
    for j in range(n):
        if c[b[i]][j] == 1:
            o += a[j]
        c[b[i]][j] = 0
print(o)
