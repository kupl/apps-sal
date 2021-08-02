from itertools import zip_longest
n = int(input())
a = list(range(n))
b = list(range(n))
c = []
for (i, j) in zip_longest(a, b):
    c.append((i + j) % n)
if len(c) != len(set(c)):
    print(-1)
else:
    print(*a)
    print(*b)
    print(*c)
