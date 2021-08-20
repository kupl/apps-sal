(n, w) = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
ss = s[0][0]
s.sort(key=lambda x: x[1], reverse=True)
t = [[] for _ in range(4)]
for u in s:
    t[u[0] - ss].append(u[1])
(l1, l2, l3, l4) = (len(t[0]) + 1, len(t[1]) + 1, len(t[2]) + 1, len(t[3]) + 1)
(a, b) = ([0] * l1, [0] * l2)
(c, d) = ([0] * l3, [0] * l4)
for i in range(1, l1):
    a[i] = t[0][i - 1] + a[i - 1]
for i in range(1, l2):
    b[i] = t[1][i - 1] + b[i - 1]
for i in range(1, l3):
    c[i] = t[2][i - 1] + c[i - 1]
for i in range(1, l4):
    d[i] = t[3][i - 1] + d[i - 1]
ans = 0
for i in range(l1):
    for j in range(l2):
        for k in range(l3):
            for l in range(l4):
                if ss * (i + j + k + l) + (j + 2 * k + 3 * l) <= w:
                    ans = max(ans, a[i] + b[j] + c[k] + d[l])
print(ans)
