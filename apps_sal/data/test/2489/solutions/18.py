import numpy as np
n = int(input())
li_a = list(map(int, input().split()))
m = max(li_a)
e = np.zeros(m)
dup = []
for a in li_a:
    if e[a - 1] == 1:
        dup.append(a - 1)
        continue
    e[a - 1] = 1
for i in dup:
    e[i] = 0
for a in set(li_a):
    origin = a
    while a <= m:
        if a == origin:
            a += origin
            continue
        e[a - 1] = 0
        a += origin
print(int(sum(e)))
