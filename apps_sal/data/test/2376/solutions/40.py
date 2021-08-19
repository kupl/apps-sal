(n, W) = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(n)]
base = a[0][0]
s = [[] for _ in range(4)]
for (w, v) in a:
    s[w - base].append(v)
for i in range(4):
    s[i].sort(reverse=True)
length = [len(s[i]) for i in range(4)]
cum = [[] for _ in range(4)]
for i in range(4):
    cum[i] = [0 for _ in range(length[i] + 1)]
    for j in range(length[i]):
        cum[i][j + 1] = cum[i][j] + s[i][j]
ans = 0
for i in range(length[0] + 1):
    for j in range(length[1] + 1):
        for k in range(length[2] + 1):
            for l in range(length[3] + 1):
                weight = (i + j + k + l) * base + j + 2 * k + 3 * l
                if weight <= W:
                    ans = max(ans, cum[0][i] + cum[1][j] + cum[2][k] + cum[3][l])
print(ans)
