from itertools import accumulate
(N, W) = map(int, input().split())
wv = {}
w1 = 0
for i in range(N):
    (w, v) = map(int, input().split())
    if i == 0:
        w1 = w
    if w in wv:
        wv[w].append(v)
    else:
        wv[w] = [v]
for w in wv:
    wv[w].sort(reverse=True)
    wv[w] = [0] + list(accumulate(wv[w]))
w2 = w1 + 1
w3 = w1 + 2
w4 = w1 + 3
for w in [w1, w1 + 1, w1 + 2, w1 + 3]:
    if w not in wv:
        wv[w] = [0]
ans = 0
for n1 in range(len(wv[w1])):
    for n2 in range(len(wv[w2])):
        for n3 in range(len(wv[w3])):
            for n4 in range(len(wv[w4])):
                w = w1 * n1 + w2 * n2 + w3 * n3 + w4 * n4
                if w <= W:
                    ans = max(ans, wv[w1][n1] + wv[w2][n2] + wv[w3][n3] + wv[w4][n4])
print(ans)
