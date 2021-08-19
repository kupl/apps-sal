N, W = list(map(int, input().split()))
wv = list(map(int, input().split()))
w1 = wv[0]

wvs = [[] for i in range(4)]
wvs[0].append(wv[1])

for i in range(N - 1):
    w, v = list(map(int, input().split()))
    w -= w1
    wvs[w].append(v)

s = [0] * 4
for i in range(4):
    wvs[i] = sorted(wvs[i], reverse=True)
    s[i] = len(wvs[i])
    if s[i] > 1:
        for j in range(1, s[i]):
            wvs[i][j] += wvs[i][j - 1]
    wvs[i].insert(0, 0)
# print(wvs)

ans = 0
for i in range(s[0] + 1):
    for j in range(s[1] + 1):
        for k in range(s[2] + 1):
            for l in range(s[3] + 1):
                weight = w1 * (i + j + k + l) + (j + 2 * k + 3 * l)
                if weight <= W:
                    value = wvs[0][i] + wvs[1][j] + wvs[2][k] + wvs[3][l]
                    ans = max(ans, value)

print(ans)
