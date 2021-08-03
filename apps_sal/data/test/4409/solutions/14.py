from collections import Counter

n = int(input())

a = [int(x) for x in input().split()]

c = Counter(a)

t = c.most_common(1)[0]

idx = a.index(t[0])

r = []

for i in range(idx - 1, -1, -1):
    if a[i] == t[0]:
        continue
    if a[i] > t[0]:
        r.append((2, i + 1, i + 2))
    else:
        r.append((1, i + 1, i + 2))

for i in range(idx + 1, n):
    if a[i] == t[0]:
        continue
    if a[i] > t[0]:
        r.append((2, i + 1, i))
    else:
        r.append((1, i + 1, i))

print(len(r))
for tt in r:
    print(*tt)
