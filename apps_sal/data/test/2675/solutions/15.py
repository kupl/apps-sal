import collections
n, m = map(int, input().split())
red = []
blue = []
for i in range(n):
    x, u = map(int, input().split())
    red.append(x * u)
for i in range(m):
    y, v = map(int, input().split())
    blue.append(y * v)
count = 0
r = dict(collections.Counter(red))
b = dict(collections.Counter(blue))
for j in r:
    if j in b:
        count += min(r[j], b[j])
print(count)
