from collections import defaultdict
s, a, b = 0, defaultdict(int), defaultdict(int)
for i in input():
    a[i] += 1
for i in input():
    b[i] += 1
for i in b:
    if i in a:
        s += min(a[i], b[i])
    else:
        s = -1
        break
print(s)
