from collections import Counter

n = int(input())
s = []
for _ in range(n):
    s.append(input())

s.sort()
c = Counter(s)

values = sorted(list(c.values()), reverse=True)
keys = sorted(list(c.keys()))
for item in c:
    if c[item] == values[0]:
        print(item)
