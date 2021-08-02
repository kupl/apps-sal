import numpy as np

n = int(input())
alist = map(int, input().split())

sort = np.zeros(10**5 + 1)
for a in alist:
    sort[a] += 1
max = 0
for i in range(10**5 - 2):
    tmp = sort[i:i + 3].sum()
    if max < tmp:
        max = tmp

print(int(max))
