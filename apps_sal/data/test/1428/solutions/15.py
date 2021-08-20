(n, c) = map(int, input().split())
d = [list(map(int, input().split())) for i in range(c)]
s = [list(map(int, input().split())) for i in range(n)]
x = [0] * c
y = [0] * c
z = [0] * c
for i in range(n):
    for j in range(n):
        a = (i + j) % 3
        if a == 0:
            x[s[i][j] - 1] += 1
        if a == 1:
            y[s[i][j] - 1] += 1
        if a == 2:
            z[s[i][j] - 1] += 1
ans = 10 ** 16
for i in range(c):
    for j in range(c):
        for k in range(c):
            if i != j and i != k and (j != k):
                o = 0
                for l in range(c):
                    o += d[l][i] * x[l]
                p = 0
                for l in range(c):
                    p += d[l][j] * y[l]
                q = 0
                for l in range(c):
                    q += d[l][k] * z[l]
                ans = min(ans, o + p + q)
print(ans)
