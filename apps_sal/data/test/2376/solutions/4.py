N, W = map(int, input().split())
d = {i: [] for i in range(0, 4)}
for i in range(N):
    w, v = map(int, input().split())
    if i == 0:
        w0 = w
    d[w - w0].append(v)

for i in range(4):
    cum = [0]
    d[i].sort(reverse=True)
    for j in d[i]:
        cum.append(cum[-1] + j)
    d[i] = cum[::]


ans = 0
for i in range(len(d[3])):
    v3_sum = d[3][i]
    w3_sum = (w0 + 3) * i
    for j in range(len(d[2])):
        v2_sum = d[2][j]
        w2_sum = (w0 + 2) * j
        for k in range(len(d[1])):
            v1_sum = d[1][k]
            w1_sum = (w0 + 1) * k

            rest = W - (w1_sum + w2_sum + w3_sum)
            if rest < 0:
                continue
            l = min(rest // w0, len(d[0]) - 1)
            v0_sum = d[0][l]

            ans = max(ans, v0_sum + v1_sum + v2_sum + v3_sum)

print(ans)
