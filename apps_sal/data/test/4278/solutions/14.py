import collections
n = int(input())
s = []
a = 0

for i in range(n):
    b = list(input())
    b.sort()
    b = str(b)
    s.append(b)

c = collections.Counter(s)

for i in c.values():
    if i > 1:
        a += i * (i - 1) // 2

print(a)
