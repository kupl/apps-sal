import numpy as np
N, M = map(int, input().split())
flag = [False] * (N + 1)
ac = 0
wa = [0] * (N + 1)
for _ in range(M):
    p, s = input().split()
    p = int(p)
    if flag[p] == False:
        if s == 'AC':
            flag[p] = True
        else:
            wa[p] += 1
print(sum(np.array(flag)), sum(np.array(wa) * np.array(flag)))
