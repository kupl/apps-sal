n, m, k = map(int, input().split())
p = []

for i in range(n):
    o = [int(w) for w in input().split()]
    p.append(o)

t = [0] * n
r = [0] * m

for i in range(k):
    a, b = map(int, input().split())
    t[a - 1] += 1
    r[b - 1] += 1

for i in range(n):
    ans = 0
    for j in range(m):
        if p[i][j] == 1:
            ans += r[j]
    print(ans - t[i], end=" ")
