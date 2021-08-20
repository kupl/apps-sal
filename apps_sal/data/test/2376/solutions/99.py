from collections import Counter
(n, W) = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]
w0 = wv[0][0]
d = {w0: [0], w0 + 1: [0], w0 + 2: [0], w0 + 3: [0]}
for (w, v) in wv:
    d[w].append(v)
for i in range(4):
    d[w0 + i].sort(reverse=True)
sd = {}
for i in range(4):
    tmp = 0
    sd[w0 + i] = [0]
    for v in d[w0 + i]:
        tmp += v
        sd[w0 + i].append(tmp)
ans = 0
for i in range(len(d[w0])):
    for j in range(len(d[w0 + 1])):
        for k in range(len(d[w0 + 2])):
            for l in range(len(d[w0 + 3])):
                if w0 * i + (w0 + 1) * j + (w0 + 2) * k + (w0 + 3) * l <= W:
                    ans = max(ans, sd[w0][i] + sd[w0 + 1][j] + sd[w0 + 2][k] + sd[w0 + 3][l])
print(ans)
