t = input()
s, k = 0, t.find('^')
for i, j in enumerate(t[: k]):
    if j != '=': s += int(j) * (k - i)
for i, j in enumerate(t[k + 1: ], 1):
    if j != '=': s -= int(j) * i
if s > 0: print('left')
elif s < 0: print('right')
else: print('balance')
