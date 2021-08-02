import collections
n = int(input())
a = list()
for i in range(n):
    a.append(int(input()))
b = collections.Counter(a)
c = list(map(lambda x: x % 2, list(b.values())))
print(c.count(1))
