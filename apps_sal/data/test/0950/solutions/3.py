(n, m) = list(map(int, input().split()))
l = [input() for _ in range(n)]
ans = n * m * n
dig = [ans for _ in range(n)]
la = [ans for _ in range(n)]
sp = [ans for _ in range(n)]
d = {}
for i in '#*&':
    d[i] = sp
for i in '0123456789':
    d[i] = dig
for i in 'abcdefghijklmnopqrstuvwxyz':
    d[i] = la
for i in range(n):
    for j in range(m):
        d[l[i][j]][i] = min(d[l[i][j]][i], min(j, m - j))
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != k and i != j and (j != k):
                ans = min(ans, dig[i] + la[j] + sp[k])
print(ans)
