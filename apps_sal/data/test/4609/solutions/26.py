n = int(input())
a = list()
for i in range(n):
    a.append(int(input()))
import collections
b = collections.Counter(a)
c = list(map(lambda x: x%2, list(b.values())))
print(c.count(1))
