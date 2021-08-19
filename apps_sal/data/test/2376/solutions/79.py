from itertools import accumulate
(n, W) = list(map(int, input().split()))
wv = [list(map(int, input().split())) for _ in range(n)]
w1 = wv[0][0]
weights = [[] for _ in range(4)]
for (w, v) in wv:
    w_diff = w - w1
    weights[w_diff].append(v)
for i in range(4):
    weights[i].sort(reverse=True)
acc = [[0] + list(accumulate(li)) for li in weights]
l3 = len(weights[3])
ans = 0
for (i, e1) in enumerate(acc[0]):
    for (j, e2) in enumerate(acc[1]):
        for (k, e3) in enumerate(acc[2]):
            w_sm = w1 * i + (w1 + 1) * j + (w1 + 2) * k
            if w_sm > W:
                break
            l = min((W - w_sm) // (w1 + 3), l3)
            val = acc[0][i] + acc[1][j] + acc[2][k] + acc[3][l]
            ans = max(ans, val)
print(ans)
