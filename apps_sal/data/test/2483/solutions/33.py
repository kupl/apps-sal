import numpy as np

n, c = map(int, input().split())

li = np.zeros(10**5 + 1, int)
ch = [[] for _ in range(10**5 + 1)]
lin = []

for _ in range(n):
    s, t, c = map(int, input().split())
    lin.append((s, t, c))

lin.sort()

for i, j, k in lin:
    if k in ch[i - 1]:
        li[i:j] += 1
        ch[j - 1].append(k)
    else:
        li[i - 1:j] += 1
        ch[j - 1].append(k)

print(np.max(li))
