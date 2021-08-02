import numpy as np

n, m = map(int, input().split())

ac = [0] * (n + 1)
wa = [0] * (n + 1)

for _ in range(m):
    p, s = map(str, input().split())
    if s == "AC" and ac[int(p)] == 0:
        ac[int(p)] = 1
    if s == "WA" and ac[int(p)] == 0:
        wa[int(p)] += 1
print(sum(ac), sum(np.array(ac) * np.array(wa)))
