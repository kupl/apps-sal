import numpy as np
(h, w) = map(int, input().split())
sn = [[0] * w for i in range(h)]
for i in range(h):
    s = input()
    for j in range(w):
        if s[j] == '.':
            sn[i][j] = 1
sn = np.array(sn)
score = np.zeros_like(sn)
total = np.zeros_like(sn)
score[0] += sn[0]
for i in range(1, h):
    score[i] = (score[i - 1] + sn[i]) * sn[i]
total += score
score[h - 1] = sn[h - 1]
for i in range(h - 2, -1, -1):
    score[i] = (score[i + 1] + sn[i]) * sn[i]
total += score
score[:, 0] = sn[:, 0]
for i in range(1, w):
    score[:, i] = (score[:, i - 1] + sn[:, i]) * sn[:, i]
total += score
score[:, w - 1] = sn[:, w - 1]
for i in range(w - 2, -1, -1):
    score[:, i] = (score[:, i + 1] + sn[:, i]) * sn[:, i]
total += score
print(total.max() - 3)
