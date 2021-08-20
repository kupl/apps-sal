import numpy as np
n = int(input())
ab = []
for _ in range(n):
    ab.append(list(map(int, input().split())))
ab = np.array(ab)
ab = ab[ab[:, 1].argsort()]
total_time = 0
flag = 0
for (_a, _b) in zip(ab[:, 0], ab[:, 1]):
    total_time += _a
    if total_time > _b:
        flag = 1
        break
if flag:
    print('No')
else:
    print('Yes')
