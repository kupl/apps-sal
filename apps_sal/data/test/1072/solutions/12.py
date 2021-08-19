(n, m) = map(int, input().split())
t = [input() for i in range(n)]
p = [''] * n
s = r = 0
for k in range(m):
    b = p[0] + t[0][k]
    for j in range(1, n):
        (a, b) = (b, p[j] + t[j][k])
        if a > b:
            s += 1
            break
    if r < s:
        r = s
    else:
        for j in range(n):
            p[j] += t[j][k]
print(s)
