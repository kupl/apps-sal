from math import ceil
(n, k) = map(int, input().split())
a = [int(i) for i in input().split()]
d = {}
for i in set(a):
    d[i] = a.count(i)
m = max(d.values())
dishes = ceil(m / k)
types = len(d)
print(types * dishes * k - n)
