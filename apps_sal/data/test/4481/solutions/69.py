import collections
n = int(input())
l = []
for i in range(n):
    l.append(input())
c = collections.Counter(l)
m = max(c.values())
chars = [key for (key, value) in c.items() if value == m]
chars.sort()
for s in chars:
    print(s)
