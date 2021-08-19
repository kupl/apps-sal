from itertools import accumulate
(h, w, k) = map(int, input().split())
s = [list(map(int, ''.join(input()))) for _ in range(h)]
min_split = 10 ** 10
for i in range(2 ** (h - 1)):
    li = []
    for j in range(h - 1):
        if i >> j & 1:
            li.append(j)
    li.append(h - 1)
    lin = [0] * w
    total = []
    over = False
    for l in range(h):
        for m in range(w):
            lin[m] += s[l][m]
            if lin[m] > k:
                over = True
        if l in li:
            total.append(lin)
            lin = [0] * w
    if over:
        continue
    now = 0
    t = len(total)
    count = t - 1
    for n in range(t):
        total[n] = [0] + list(accumulate(total[n]))
    for o in range(1, w + 1):
        for p in range(t):
            if total[p][o] - total[p][now] > k:
                now = o - 1
                count += 1
                break
    min_split = min(min_split, count)
print(min_split)
