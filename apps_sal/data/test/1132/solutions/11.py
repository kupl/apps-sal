(n, m) = input().split()
n = int(n)
m = int(m)
a = [0] * n
for i in range(0, m):
    (x, y) = input().split()
    x = int(x)
    y = int(y)
    a[x - 1] += 1
    a[y - 1] += 1
r = 'unknown'
s = set(a)
if s == {2}:
    r = 'ring'
if s == {1, 2}:
    r = 'bus'
if s == {1, m}:
    r = 'star'
print(r, 'topology')
