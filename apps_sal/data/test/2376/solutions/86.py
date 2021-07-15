from itertools import accumulate

n, W = list(map(int, input().split()))
wv = [list(map(int, input().split())) for _ in range(n)]

w1 = wv[0][0]
weights = [[] for _ in range(4)]

for w, v in wv:
    w_diff = w - w1
    weights[w_diff].append(v)

for i in range(4):
    weights[i].sort(reverse=True)

acc = [[0] + list(accumulate(li)) for li in weights]

ans = 0
for i, e1 in enumerate(acc[0]):
    for j, e2 in enumerate(acc[1]):
        for k, e3 in enumerate(acc[2]):
            for l, e4 in enumerate(acc[3]):
                if w1 * i + (w1 + 1) * j + (w1 + 2) * k + (w1 + 3) * l <= W:
                    ans = max(ans, e1 + e2 + e3 + e4)

print(ans)

